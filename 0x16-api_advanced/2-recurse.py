#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mally13"
    }
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 404:
            return None
        data = response.json()["data"]["children"]
        for post in data:
            hot_list.append(post["data"]["title"])
            recurse(post["data"]["title"], hot_list)
        return hot_list
    except Exception as e:
        return None
