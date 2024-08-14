#!/usr/bin/python3
"""
This module contains a function
def top_ten(subreddit) that prints titles
"""
import requests


def top_ten(subreddit):
    """
    subreddit = str
    prints title
    """
    url = ("https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    headers = {'User-Agent': 'Mozila/5.0'}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    resp_js = resp.json()
    if resp.status_code == 200 and resp.json()["data"]:
        for post in resp_js['data'].get('children'):
            print(post.get('data').get('title'))
    else:
        print(None)
