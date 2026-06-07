# Wiki-Study OS

Wiki-Study OS is a local-first PyQt6 desktop application that turns study materials into a searchable Markdown wiki. Core features work without an LLM or cloud account.

## Features

- Import PDF, DOCX, PPTX, TXT, Markdown, images, websites, YouTube videos, GitHub repositories, and GitLab repositories.
- Store every source as a Markdown note in `vault/`, with extracted images in `vault/assets/`.
- Edit notes with autosave, preview Obsidian-style `[[wiki links]]`, inspect backlinks through the core API, and create automatic cross-note links.
- Search locally with BM25 keyword search and optional sentence-transformer semantic search.
- View embedded global and current-note graphs colored by study status. Drag to pan, scroll to zoom, and double-click nodes to open notes.
- Run Python fenced code blocks sequentially in a note-scoped lab session.
- Run PowerShell commands from a persistent terminal inside the app.
- Save drawing sessions as image-backed workspace notes.
- Use deterministic local summaries, quizzes, and flashcards; optionally use Ollama through LiteLLM.

## Install

Python 3.10 or newer is recommended.

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Some optional packages are large. EasyOCR is loaded only when OCR is needed, sentence-transformers is loaded only for semantic indexing, and LiteLLM is loaded only for optional AI study tools.

## Run

```powershell
run.bat
```

`run.bat` launches the desktop app in the background and closes its command window immediately. `run_study.bat` is the underlying launcher.

Or:

```powershell
venv\Scripts\python.exe -m app.gui.native_gui
```

Useful CLI commands:

```powershell
venv\Scripts\python.exe main.py list
venv\Scripts\python.exe main.py ingest "notes.pdf"
venv\Scripts\python.exe main.py clip "https://example.com/article"
venv\Scripts\python.exe main.py search "attention mechanism" --mode keyword
venv\Scripts\python.exe main.py graph
venv\Scripts\python.exe main.py index --semantic
```

## Optional Ollama

Run Ollama locally and set a LiteLLM-compatible model before launching:

```powershell
$env:LLM_MODEL = "ollama/llama3.2"
```

The default is already `ollama/llama3.2`. Missing models fail gracefully and do not affect core wiki features.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the module map and design notes.
