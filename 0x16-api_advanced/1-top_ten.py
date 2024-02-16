#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mally13"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            print("None")
        data = response.json()["data"]["children"]
        for post in data:
            print(post["data"]["title"])
    except:
        return
