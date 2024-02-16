#!/usr/bin/python3
"""Returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    reddit_url_req = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        response = requests.get(reddit_url_req, allow_redirects=False)
        if response.status_code == 200:
            subreddit_data = response.json()["data"]
            return subreddit_data["subscribers"]
        else:
            return 0
    except Exception as e:
        return 0
