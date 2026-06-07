import argparse
import sys
from pathlib import Path

from app.core.config import VAULT_PATH
from app.core.sandbox_manager import SandboxManager
from app.core.search_engine import SearchEngine
from app.core.study_tools import StudyTools
from app.core.wiki_manager import WikiManager
from ingestion.clipper import WebClipper
from ingestion.ingestor import Ingestor


def build_parser():
    parser = argparse.ArgumentParser(description="Wiki-Study OS command line tools")
    commands = parser.add_subparsers(dest="command", required=True)
    ingest = commands.add_parser("ingest"); ingest.add_argument("path")
    clip = commands.add_parser("clip"); clip.add_argument("url")
    commands.add_parser("list")
    status = commands.add_parser("status"); status.add_argument("topic"); status.add_argument("state", choices=["read", "reading", "unread", "pending"])
    search = commands.add_parser("search"); search.add_argument("query"); search.add_argument("--mode", choices=["keyword", "hybrid", "semantic"], default="keyword")
    index = commands.add_parser("index"); index.add_argument("--semantic", action="store_true")
    commands.add_parser("link")
    graph = commands.add_parser("graph"); graph.add_argument("--focus")
    quiz = commands.add_parser("quiz"); quiz.add_argument("topic"); quiz.add_argument("--n", type=int, default=5)
    cards = commands.add_parser("flashcards"); cards.add_argument("topic")
    summary = commands.add_parser("summary"); summary.add_argument("topic")
    cells = commands.add_parser("cells"); cells.add_argument("topic")
    run = commands.add_parser("run"); run.add_argument("topic"); run.add_argument("index", type=int)
    return parser


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args()
    wiki, ingestor = WikiManager(VAULT_PATH), Ingestor(VAULT_PATH)
    if args.command == "ingest":
        print(ingestor.ingest(Path(args.path)))
    elif args.command == "clip":
        print(WebClipper(VAULT_PATH).clip(args.url))
    elif args.command == "list":
        print("\n".join(wiki.get_all_pages()))
    elif args.command == "status":
        print(wiki.update_status(args.topic, args.state))
    elif args.command == "link":
        wiki.auto_link_all()
    elif args.command == "graph":
        print(wiki.generate_graph(focus=args.focus))
    elif args.command in {"search", "index"}:
        search = SearchEngine(VAULT_PATH)
        if args.command == "index":
            print(f"Indexed {search.build_index(semantic=args.semantic)} chunks")
        else:
            for result in search.search_local(args.query, mode=args.mode):
                print(f"[{result['source']}] {result['score']:.3f}\n{result['text'][:300]}\n")
    elif args.command in {"quiz", "flashcards", "summary"}:
        study = StudyTools(VAULT_PATH)
        if args.command == "quiz": print(study.generate_quiz(args.topic, args.n))
        elif args.command == "flashcards": print(study.generate_flashcards(args.topic))
        else: print(study.generate_summary(args.topic))
    elif args.command in {"cells", "run"}:
        sandbox = SandboxManager(VAULT_PATH)
        print(sandbox.list_cells(args.topic) if args.command == "cells" else sandbox.run_cell(args.topic, args.index))


if __name__ == "__main__":
    main()
