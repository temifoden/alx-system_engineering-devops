#!/usr/bin/python3
import requests
"""
A function that make requests
"""

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
    url = f"https://www.reddit.com/r/{subreddit}/about.json?limit=0"
    # Set custom user-agent to avoid "Too many Requests" errors
    headers = {"User-Agent": "My Reddit API Client"}

    # Send a GET request without following redirects
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Raise an exception for non-200 status code
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error requesting subreddit info: {e}")
        return 0

    # check if response is Successful (200 OK) and parse JSON
    if response.status_code == 200:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        print(f"Invalid subreddit or API error(status code:
              {response.status_code})")
        return 0
