#!/usr/bin/python3
"""Function that queries Reddit API and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    resp_ret = requests.get(reddit_url, headers=headers, allow_redirects=False)
    if resp_ret.status_code == 404:
        return 0
    results = resp_ret.json().get("data")
    return results.get("subscribers")
