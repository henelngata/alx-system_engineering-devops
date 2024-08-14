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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            if not posts:
                print(None)
                return
            for post in posts:
                print(post['data']['title'])
        elif response.status_code in [301, 404]:
            print(None)
        else:
            print(None)
    except requests.exceptions.RequestException:
        print(None)
