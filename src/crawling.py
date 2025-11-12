# crawling.py
from itertools import islice
from youtube_comment_downloader import *
import json

def crawl_comments(url: str, output_file: str = "ENDEVR.json", limit: int = None):
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(url, sort_by=SORT_BY_POPULAR)
    
    if limit:
        comments = islice(comments, limit)
    
    comments_list = list(comments)

    with open(output_file, "w", encoding="utf-8") as f:
        for comment in comments_list:
            json_line = json.dumps(comment, ensure_ascii=False)
            f.write(json_line + "\n")

    print(f"✅ Saved {len(comments_list)} comments to '{output_file}' (JSON Lines format)")

if __name__ == "__main__":
    crawl_comments("https://www.youtube.com/watch?v=LTduwK0-sGI")
