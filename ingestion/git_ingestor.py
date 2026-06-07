import os
import re
import shutil
from pathlib import Path

from git import Repo

from ingestion.ingestor import Ingestor


class GitIngestor:
    SUPPORTED = {".py", ".js", ".ts", ".c", ".cpp", ".h", ".hpp", ".java", ".go", ".rs",
                 ".md", ".txt", ".rst", ".sh", ".bat", ".ps1", ".sql", ".yaml", ".yml", ".json"}

    def __init__(self, vault_path="vault"):
        self.vault_path = Path(vault_path)
        self.ingestor = Ingestor(vault_path)
        self.temp_dir = Path.cwd() / "temp_git_repos"

    @staticmethod
    def extract_repo_name(url):
        match = re.search(r"/([^/]+?)(?:\.git)?/?$", url)
        return match.group(1) if match else "repository"

    @staticmethod
    def _remove_readonly(func, path, _):
        os.chmod(path, 0o700)
        func(path)

    def ingest(self, url):
        repo_name = self.extract_repo_name(url)
        self.temp_dir.mkdir(exist_ok=True)
        repo_path = self.temp_dir / repo_name
        if repo_path.exists():
            shutil.rmtree(repo_path, onerror=self._remove_readonly)
        try:
            Repo.clone_from(url, repo_path, depth=1)
            files = []
            for path in repo_path.rglob("*"):
                if path.is_file() and ".git" not in path.parts and path.suffix.lower() in self.SUPPORTED:
                    files.append(path)
            overview = [f"# {repo_name}\n", "#pending\n", f"Source: {url}\n", "## Repository Structure\n"]
            for path in sorted(files):
                rel = path.relative_to(repo_path).as_posix()
                note_title = self.ingestor.sanitize_title(f"{repo_name} - {rel.replace('/', ' - ')}")
                content = path.read_text(encoding="utf-8", errors="ignore")
                lang = path.suffix.lstrip(".")
                note = f"# {rel}\n\n#pending\n\nSource: {url}\n\n```{lang}\n{content}\n```\n"
                self.ingestor.save_markdown(note_title, note, url, "repository_file")
                overview.append(f"- [[{note_title}|{rel}]]\n")
            self.ingestor.save_markdown(repo_name, "\n".join(overview), url, "repository")
            return repo_name
        finally:
            if repo_path.exists():
                shutil.rmtree(repo_path, onerror=self._remove_readonly)
