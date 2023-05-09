#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """prints a sorted count of given keywords"""
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
    try:
        results = resp_ret.json()
        if resp_ret.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for ch in results.get("children"):
        title = ch.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([tms for tms in title if tms == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
