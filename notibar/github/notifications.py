
from urllib import response

import requests

from github.credentials import get_github_token


def get_github_notifications():
    """
    Fetch GitHub notifications using the provided token.
    """
    token = get_github_token()
    if not token:
        print("No GitHub token found.")
        return []
    
    response = requests.get(
        "https://api.github.com/notifications",
        headers={"Authorization": f"token {token}"},
        params={"participating": "true"}
    )

    if response.status_code != 200:
        print(f"Error fetching notifications: {response.status_code}")
        return []
    
    print(f"Fetched {len(response.json())} notifications.")
    print(response.json())
    return response.json()