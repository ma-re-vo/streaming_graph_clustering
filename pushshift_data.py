import requests
import json
import time

url = "https://api.pushshift.io/reddit/search/submission/"

def collect(subreddit="python", limit=1000, batch_size=100):
    all_data = []
    before = None

    while len(all_data) < limit:
        params = {
            "subreddit": subreddit,
            "size": batch_size,
            "sort": "desc",
            "sort_type": "created_utc"
        }

        if before:
            params["before"] = before

        r = requests.get(url, params=params)
        data = r.json().get("data", [])

        if not data:
            break

        all_data.extend(data)
        before = data[-1]["created_utc"]

        print(f"Collected: {len(all_data)}")
        time.sleep(1)

    return all_data


data = collect(limit=2000)

with open("reddit_dump.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item) + "\n")