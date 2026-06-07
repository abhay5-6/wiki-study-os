from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parents[2]
VAULT_PATH = Path(os.getenv("WIKI_STUDY_VAULT", ROOT_DIR / "vault")).resolve()
ASSETS_PATH = VAULT_PATH / "assets"
DATA_PATH = ROOT_DIR / "data"
INDEX_PATH = DATA_PATH / "index"
CACHE_PATH = DATA_PATH / "cache"

SUPPORTED_TEXT = {".txt", ".md", ".rst"}
SUPPORTED_IMAGES = {".png", ".jpg", ".jpeg", ".bmp", ".webp"}
SUPPORTED_DOCS = {".pdf", ".docx", ".pptx"}
OCR_LANGUAGES = ["en"]

MAX_WORDS_PER_CHUNK = 400
CHUNK_OVERLAP = 60
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
TOP_K_RETRIEVAL = 10
BM25_WEIGHT = 0.45
EMBEDDING_WEIGHT = 0.55

DEFAULT_MODEL = os.getenv("LLM_MODEL", "ollama/llama3.2")
OLLAMA_API_BASE = os.getenv("OLLAMA_API_BASE", "http://localhost:11434")
SANDBOX_TIMEOUT = 15
GRAPH_OUTPUT = CACHE_PATH / "vault_graph.html"
LOCAL_GRAPH_OUTPUT = CACHE_PATH / "local_graph.html"

for path in (VAULT_PATH, ASSETS_PATH, DATA_PATH, INDEX_PATH, CACHE_PATH):
    path.mkdir(parents=True, exist_ok=True)
