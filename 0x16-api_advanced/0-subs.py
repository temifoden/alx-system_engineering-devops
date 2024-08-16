#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API nd returns the number of subscribers
    for a given subreddit.
    It handles invalid subreddits and redirects.
    Args:
    subreddit: the name of the subreddit to query
    Return:
    The number of subcribers (integer) or 0 if the subreddit is invalid
    """

    # Base URl for subreddint information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set custom user-agent to avoid "Too many Requests" errors
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    # Send a GET request without following redirects
   
    response = requests.get(url, headers=headers, allow_redirects=False)
        # Raise an exception for non-200 status code
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
