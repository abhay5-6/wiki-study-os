import requests
from bs4 import BeautifulSoup
import re
import os
from datetime import datetime
from ingestion.youtube_ingestor import YouTubeIngestor
from ingestion.git_ingestor import GitIngestor

class WebClipper:
    def __init__(self, vault_path="vault"):
        self.vault_path = vault_path
        self.yt_ingestor = YouTubeIngestor(vault_path)
        self.git_ingestor = GitIngestor(vault_path)

    def is_youtube_url(self, url):
        return "youtube.com" in url or "youtu.be" in url

    def is_git_url(self, url):
        return url.endswith(".git") or "github.com" in url or "gitlab.com" in url

    def clip(self, url):
        if self.is_youtube_url(url):
            return self.yt_ingestor.ingest(url)
        if self.is_git_url(url):
            return self.git_ingestor.ingest(url)
        
        print(f"Clipping content from: {url}")
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()

            title = soup.title.string if soup.title else "Untitled_Web_Clip"
            title = re.sub(r'[\\/*?:"<>|]', "", title).strip()
            
            # Extract main text
            # This is a basic approach; more advanced libraries like 'trafilatura' could be used
            paragraphs = soup.find_all('p')
            text_content = "\n\n".join([p.get_text().strip() for p in paragraphs if len(p.get_text()) > 20])

            if not text_content:
                # Fallback to general text if no paragraphs found
                text_content = soup.get_text(separator='\n\n', strip=True)

            metadata = f"---\nsource: {url}\ndate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\ntype: web_clip\n---\n\n"
            content = f"# {title}\n\n{text_content}"
            
            safe_title = title[:100] # Limit filename length
            target_path = os.path.join(self.vault_path, f"{safe_title}.md")
            
            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(metadata + content)
            
            print(f"Saved web clip: {safe_title}.md")
            return safe_title

        except Exception as e:
            print(f"Failed to clip URL: {e}")
            return None
