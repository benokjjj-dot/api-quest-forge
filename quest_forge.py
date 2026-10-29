#!/usr/bin/env python3
"""Quest Forge — генератор квестов из публичного API."""

import json
import random
import urllib.request

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts():
    with urllib.request.urlopen(API_URL, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def forge_quest(posts):
    post = random.choice(posts)
    return {
        "id": post["id"],
        "title": post["title"],
        "body": post["body"],
        "quest": f"Найти исполнителя для: {post['title']}",
    }


def main():
    posts = fetch_posts()
    quest = forge_quest(posts)
    print(json.dumps(quest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
