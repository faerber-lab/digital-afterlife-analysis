from itertools import islice
from youtube_comment_downloader import *
downloader = YoutubeCommentDownloader()
comments = downloader.get_comments_from_url('https://www.youtube.com/watch?v=LTduwK0-sGI', sort_by=SORT_BY_POPULAR)

for comment in islice(comments, 10):
    print(comment)

comments_list = list(comments)

output_file = "ENDEVR.json"
with open(output_file, "w", encoding="utf-8") as f:
    for comment in comments_list:
        json_line = json.dumps(comment, ensure_ascii=False)
        f.write(json_line + "\n")

print(f"Saved {len(comments_list)} comments to '{output_file}'")
