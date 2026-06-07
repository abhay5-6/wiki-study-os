# Wiki-Study OS Architecture

## Local-First Data Flow

1. Importers convert files and URLs into Markdown notes.
2. Notes are stored in `vault/`; binary images are stored in `vault/assets/`.
3. `WikiManager` handles page lifecycle, statuses, links, backlinks, and graph generation.
4. `SearchEngine` builds a BM25 index and optionally adds sentence-transformer embeddings.
5. The PyQt6 desktop app coordinates editing, ingestion, search, research, graphs, drawing, notebook execution, and a persistent PowerShell terminal.

## Modules

- `app/gui/native_gui.py`: nine-section desktop application with native Qt global and local graph canvases.
- `app/core/config.py`: root paths and environment-backed configuration.
- `app/core/wiki_manager.py`: Markdown wiki operations and PyVis graph generation.
- `app/core/search_engine.py`: local keyword and optional semantic search plus web result lookup.
- `app/core/study_tools.py`: deterministic and optional LiteLLM study aids.
- `app/core/sandbox_manager.py`: note-scoped sequential Python cell sessions.
- `app/core/ink_engine.py`: mouse and stylus-compatible Qt drawing canvas.
- `ingestion/ingestor.py`: PDF, DOCX, PPTX, text, Markdown, and image ingestion.
- `ingestion/clipper.py`: URL dispatch and article extraction.
- `ingestion/youtube_ingestor.py`: timestamped transcripts and optional study-frame capture.
- `ingestion/git_ingestor.py`: shallow repository clone and file-note generation.

## Performance Notes

Keyword search is available immediately and can be rebuilt locally. Semantic embeddings are cached under `data/index/` and are optional. OCR, video processing, embeddings, and LLM calls are loaded only when their feature is used.

## Security Note

The Lab Notebook retains variables between cells for study convenience. It executes local Python code in-process and should only run code you trust.
