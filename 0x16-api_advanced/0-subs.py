#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    reddit_url_req = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mally13"
    }
    response = requests.get(reddit_url_req, headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return 0
    subreddit_data = response.json()["data"]
    return subreddit_data["subscribers"]
