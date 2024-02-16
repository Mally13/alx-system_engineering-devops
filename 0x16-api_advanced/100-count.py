#!/usr/bin/python3
"""
Queries the Reddit API and parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
Javascript should count as javascript, but java should not)
"""
import requests


def count_words(subreddit, word_list, word_count=None):
    if word_count is None:
        word_count = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "Mally13"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json()["data"]["children"]
        for post in data:
            count_words_in_post(post["data"]["title"].lower(),
                                word_list, word_count)
            count_words(post["data"]["title"].lower(), word_list, word_count)
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
    except Exception as e:
        return


def count_words_in_post(title_lower, word_list, word_count):
    for word in word_list:
        if word.lower() in title_lower.split():
            word_count[word.lower()] = word_count.get(word.lower(), 0) + 1
    return word_count
