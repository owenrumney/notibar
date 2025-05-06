
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
    # print("Notifications:", response.json())
    return response.json()

def get_html_url(url):
    """
    Convert a URL to HTML format.
    """
    token = get_github_token()
    if not token:
        print("No GitHub token found.")
        return ""
    response = requests.get(
        url,
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json"},
    )
    if response.status_code != 200:
        print(f"Error fetching HTML URL: {response.status_code}")
        return ""
    html_url = response.json().get("html_url")
    if not html_url:
        print("No HTML URL found in the response.")
        return ""
    return html_url

def mark_notification_as_done(notification_id):
    """
    Mark a notification as done.
    """
    token = get_github_token()
    if not token:
        print("No GitHub token found.")
        return False
    
    response = requests.delete(
        f"https://api.github.com/notifications/threads/{notification_id}",
        headers={"Authorization": f"token {token}", "Accept": "application/vnd.github+json"},

    )

    if response.status_code != 204:
        print(f"Error marking notification as done: {response.status_code}")
        return False
    
    print(f"Marked notification {notification_id} as done.")
    return True