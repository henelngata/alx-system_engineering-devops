#!/usr/bin/python3
"""This module contains a module
number_of_subscribers(subbreddit)
that queries the Reddit API and returns
the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Has one param
    subreddit = "str"
    """
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url=url, headers=headers, allow_redirects=False)
    if resp.status_code == 200 and resp.json()["data"]:
        return (resp.json()["data"]["subscribers"])
    else:
        return 0
