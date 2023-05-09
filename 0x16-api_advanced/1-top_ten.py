#!/usr/bin/python3
"""Function that prints top 10 posts on a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 posts"""
    query_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    first_ten = {
        "limit": 10
    }
    resp_ret = requests.get(query_url, headers=headers, params=first_ten,
                            allow_redirects=False)
    if resp_ret.status_code == 404:
        print("None")
        return
    results = resp_ret.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
