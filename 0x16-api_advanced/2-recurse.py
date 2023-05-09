#!/usr/bin/python3
"""A recursive function to query a list of posts on a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns titles of posts on a subreddit."""
    query_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    para_meters = {
        "after": after,
        "count": count,
        "limit": 100
    }
    resp_ret = requests.get(query_url, headers=headers, params=para_meters,
                            allow_redirects=False)
    if resp_ret.status_code == 404:
        return None

    results = resp_ret.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
