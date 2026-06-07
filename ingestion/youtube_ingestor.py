import re
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import cv2
import yt_dlp
import numpy as np
from app.core.config import ASSETS_PATH

class YouTubeIngestor:
    def __init__(self, vault_path="vault"):
        self.vault_path = vault_path
        self.assets_path = os.path.join(vault_path, "assets")
        os.makedirs(self.assets_path, exist_ok=True)

    def extract_video_id(self, url):
        regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
        match = re.search(regex, url)
        return match.group(1) if match else None

    def get_video_metadata(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find("meta", property="og:title")
            if title:
                return title["content"]
            title_tag = soup.find("title")
            if title_tag:
                return title_tag.text.replace(" - YouTube", "")
            return "YouTube Video"
        except Exception:
            return "YouTube Video"

    def format_timestamp(self, seconds):
        td = datetime.utcfromtimestamp(seconds)
        if seconds < 3600:
            return td.strftime('%M:%S')
        return td.strftime('%H:%M:%S')

    def is_text_rich(self, frame):
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Use Canny to find edges
        edges = cv2.Canny(gray, 50, 150)
        # Calculate edge density
        density = np.sum(edges > 0) / edges.size
        # Slides/Notes typically have higher edge density due to text (0.015 - 0.05)
        return density > 0.012

    def capture_important_frames(self, url, video_id, title_slug):
        print(f"Analyzing video for slides and notes (this may take a minute)...")
        ydl_opts = {
            'format': 'best[height<=480]', # Slightly higher res for text clarity
            'quiet': True,
            'no_warnings': True,
        }
        
        captured_images = {}
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                stream_url = info['url']
                duration = info.get('duration', 0)

            cap = cv2.VideoCapture(stream_url)
            if not cap.isOpened():
                return captured_images

            # Heuristics for "Important" Study Frames:
            # 1. Stability: The frame doesn't change much for a few seconds (likely a slide).
            # 2. Novelty: The frame is different from the last saved one.
            # 3. Text/Edge Density: The frame likely contains text or diagrams.
            
            last_frame_gray = None
            last_saved_frame_gray = None
            interval = 5 # seconds
            
            for sec in range(0, int(duration), interval):
                cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
                ret, frame = cap.read()
                if not ret: continue
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray_blurred = cv2.GaussianBlur(gray, (21, 21), 0)
                
                if last_frame_gray is None:
                    # First frame ever
                    if self.is_text_rich(frame):
                        img_name = f"{title_slug}_ts_{sec}.jpg"
                        cv2.imwrite(os.path.join(self.assets_path, img_name), frame)
                        captured_images[sec] = img_name
                        last_saved_frame_gray = gray_blurred
                    last_frame_gray = gray_blurred
                    continue

                # 1. Check Stability (compared to 5s ago)
                diff_prev = cv2.absdiff(last_frame_gray, gray_blurred)
                stability_score = (np.sum(diff_prev > 25) / diff_prev.size) * 100
                
                # 2. Check Novelty (compared to last saved)
                novelty_score = 100
                if last_saved_frame_gray is not None:
                    diff_saved = cv2.absdiff(last_saved_frame_gray, gray_blurred)
                    novelty_score = (np.sum(diff_saved > 25) / diff_saved.size) * 100

                # A "Note/Slide" is Stable (< 10% change) and Novel (> 15% change from last saved)
                if stability_score < 8.0 and novelty_score > 15.0:
                    if self.is_text_rich(frame):
                        img_name = f"{title_slug}_ts_{sec}.jpg"
                        cv2.imwrite(os.path.join(self.assets_path, img_name), frame)
                        captured_images[sec] = img_name
                        last_saved_frame_gray = gray_blurred
                        print(f"  [Captured] New slide/note detected at {self.format_timestamp(sec)}")

                last_frame_gray = gray_blurred
            
            cap.release()
        except Exception as e:
            print(f"Warning: Could not capture frames: {e}")
        
        return captured_images

    def ingest(self, url):
        video_id = self.extract_video_id(url)
        if not video_id:
            print("Invalid YouTube URL")
            return None

        print(f"Fetching transcript for YouTube video: {video_id}")
        try:
            title = self.get_video_metadata(url)
            safe_title = re.sub(r'[\\/*?:"<>|]', "", title).strip()[:100]
            title_slug = re.sub(r'[^a-z0-9]+', '_', safe_title.lower())

            # 1. Capture frames first
            images = self.capture_important_frames(url, video_id, title_slug)

            # 2. Get Transcript
            transcript_list = YouTubeTranscriptApi().fetch(video_id)
            
            formatted_transcript = "> [!quote] Annotated Transcript\n> \n"
            last_timestamp = -60
            
            # Keep track of which images we've used
            available_secs = sorted(images.keys())
            
            for entry in transcript_list:
                current_start = entry.start
                
                # Check if we should insert an image before this text
                while available_secs and available_secs[0] <= current_start:
                    sec = available_secs.pop(0)
                    img_name = images[sec]
                    formatted_transcript += f"> ![[{img_name}]]\n> *Visual at {self.format_timestamp(sec)}*\n> \n"

                # Add a timestamp label every ~1 minute
                if current_start - last_timestamp >= 60:
                    timestamp = self.format_timestamp(current_start)
                    formatted_transcript += f"> \n> **[{timestamp}]** "
                    last_timestamp = current_start
                
                formatted_transcript += entry.text.replace('\n', ' ') + " "

            # Add any remaining images at the end
            for sec in available_secs:
                img_name = images[sec]
                formatted_transcript += f"\n\n![[{img_name}]]\n*Visual at {self.format_timestamp(sec)}*\n\n"

            metadata = f"---\nsource: {url}\ndate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\ntype: youtube_video\nvideo_id: {video_id}\n---\n\n"
            content = f"# {title}\n\n"
            content += f"## 🔗 Video Link\n[Watch on YouTube]({url})\n\n"
            content += formatted_transcript

            target_path = os.path.join(self.vault_path, f"{safe_title}.md")
            
            # Ensure unique filename if title exists
            base_safe_title = safe_title
            counter = 1
            while os.path.exists(target_path):
                safe_title = f"{base_safe_title}_{counter}"
                target_path = os.path.join(self.vault_path, f"{safe_title}.md")
                counter += 1

            with open(target_path, 'w', encoding='utf-8') as f:
                f.write(metadata + content)
            
            print(f"Saved annotated YouTube transcript: {safe_title}.md")
            return safe_title
        except Exception as e:
            print(f"Failed to ingest YouTube video: {e}")
            import traceback
            traceback.print_exc()
            return None
