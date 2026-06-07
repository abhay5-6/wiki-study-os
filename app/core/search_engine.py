import json
import logging
import pickle
import re
from pathlib import Path

import numpy as np
from rank_bm25 import BM25Okapi

from app.core.config import (
    BM25_WEIGHT,
    EMBEDDING_MODEL,
    EMBEDDING_WEIGHT,
    INDEX_PATH,
    MAX_WORDS_PER_CHUNK,
    CHUNK_OVERLAP,
    TOP_K_RETRIEVAL,
    VAULT_PATH,
)

logger = logging.getLogger("SearchEngine")


class SearchEngine:
    def __init__(self, vault_path=VAULT_PATH, enable_semantic=True):
        self.vault_path = Path(vault_path)
        self.enable_semantic = enable_semantic
        self._model = None
        self.chunks = []
        self.embeddings = None
        self.bm25 = None
        index_path = INDEX_PATH if self.vault_path.resolve() == Path(VAULT_PATH).resolve() else self.vault_path / ".wiki-study" / "index"
        index_path.mkdir(parents=True, exist_ok=True)
        self.emb_path = index_path / "embeddings.npy"
        self.chunk_path = index_path / "chunks.pkl"
        self.meta_path = index_path / "metadata.json"
        self.load_index()

    @property
    def model(self):
        if self._model is None:
            from sentence_transformers import SentenceTransformer
            self._model = SentenceTransformer(EMBEDDING_MODEL)
        return self._model

    def chunk_text(self, text):
        words = text.split()
        if len(words) <= MAX_WORDS_PER_CHUNK:
            return [text]
        step = MAX_WORDS_PER_CHUNK - CHUNK_OVERLAP
        return [" ".join(words[start:start + MAX_WORDS_PER_CHUNK]) for start in range(0, len(words), step)]

    def scan_vault(self):
        records = []
        for file in sorted(self.vault_path.glob("*.md")):
            try:
                text = file.read_text(encoding="utf-8")
                for idx, chunk in enumerate(self.chunk_text(text)):
                    records.append({"source": file.stem, "chunk_id": idx, "text": chunk})
            except OSError as exc:
                logger.warning("Failed reading %s: %s", file, exc)
        return records

    def _build_bm25(self):
        tokenized = [self.tokenize(c["text"]) for c in self.chunks]
        self.bm25 = BM25Okapi(tokenized) if tokenized else None

    @staticmethod
    def tokenize(text):
        return re.findall(r"\w+", text.lower())

    def build_index(self, semantic=None):
        self.chunks = self.scan_vault()
        self._build_bm25()
        use_semantic = self.enable_semantic if semantic is None else semantic
        self.embeddings = None
        if self.chunks and use_semantic:
            try:
                self.embeddings = self.model.encode([c["text"] for c in self.chunks], convert_to_numpy=True)
            except Exception as exc:
                logger.warning("Semantic indexing unavailable, keeping keyword index: %s", exc)
        self.save_index()
        return len(self.chunks)

    def save_index(self):
        self.chunk_path.parent.mkdir(parents=True, exist_ok=True)
        if self.embeddings is not None:
            np.save(self.emb_path, self.embeddings)
        elif self.emb_path.exists():
            self.emb_path.unlink()
        with self.chunk_path.open("wb") as handle:
            pickle.dump(self.chunks, handle)
        self.meta_path.write_text(json.dumps({"num_chunks": len(self.chunks)}, indent=2), encoding="utf-8")

    def load_index(self):
        try:
            if self.chunk_path.exists():
                with self.chunk_path.open("rb") as handle:
                    self.chunks = pickle.load(handle)
                self._build_bm25()
            if self.emb_path.exists():
                self.embeddings = np.load(self.emb_path, allow_pickle=False)
                if len(self.embeddings) != len(self.chunks):
                    self.embeddings = None
        except Exception as exc:
            logger.warning("Ignoring invalid search index: %s", exc)
            self.chunks, self.embeddings, self.bm25 = [], None, None

    @staticmethod
    def cosine_similarity(query_embedding, matrix):
        query = query_embedding / (np.linalg.norm(query_embedding) + 1e-10)
        normalized = matrix / (np.linalg.norm(matrix, axis=1, keepdims=True) + 1e-10)
        return np.dot(normalized, query)

    def search_local(self, query, top_k=TOP_K_RETRIEVAL, mode="hybrid"):
        if not self.chunks:
            self.build_index(semantic=False)
        if not self.chunks or not self.bm25:
            return []
        query_tokens = self.tokenize(query)
        bm25_scores = np.array(self.bm25.get_scores(query_tokens), dtype=float)
        overlap_scores = np.array([
            len(set(query_tokens) & set(self.tokenize(chunk["text"]))) / max(len(set(query_tokens)), 1)
            for chunk in self.chunks
        ])
        if bm25_scores.size:
            bm25_scores -= bm25_scores.min()
            if bm25_scores.max() > 0:
                bm25_scores /= bm25_scores.max()
        lexical_scores = np.maximum(bm25_scores, overlap_scores)
        scores = lexical_scores
        if mode != "keyword" and self.embeddings is not None:
            try:
                semantic = self.cosine_similarity(self.model.encode(query, convert_to_numpy=True), self.embeddings)
                scores = semantic if mode == "semantic" else BM25_WEIGHT * lexical_scores + EMBEDDING_WEIGHT * semantic
            except Exception as exc:
                logger.warning("Semantic query unavailable: %s", exc)
        indices = np.argsort(scores)[::-1][:top_k]
        return [{**self.chunks[idx], "score": float(scores[idx])} for idx in indices if scores[idx] > 0 or mode != "keyword"]

    def search_web(self, query, max_results=5):
        try:
            from duckduckgo_search import DDGS
            with DDGS() as ddgs:
                return [{"title": r.get("title", ""), "href": r.get("href", ""), "body": r.get("body", "")}
                        for r in ddgs.text(query, max_results=max_results)]
        except Exception as exc:
            logger.warning("Web search failed: %s", exc)
            return []
