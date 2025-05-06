
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
        # params={"participating": "true"}
    )

    if response.status_code != 200:
        print(f"Error fetching notifications: {response.status_code}")
        return []
    
    print(f"Fetched {len(response.json())} notifications.")
    return response.json()

def mark_notification_as_read(notification_id):
    """
    Mark a notification as read.
    """
    token = get_github_token()
    if not token:
        print("No GitHub token found.")
        return False
    
    response = requests.patch(
        f"https://api.github.com/notifications/threads/{notification_id}",
        headers={"Authorization": f"token {token}"},
        json={"read": True}
    )

    if response.status_code != 205:
        print(f"Error marking notification as read: {response.status_code}")
        return False
    
    print(f"Marked notification {notification_id} as read.")
    return True

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

    if response.status_code != 205:
        print(f"Error marking notification as done: {response.status_code}")
        return False
    
    print(f"Marked notification {notification_id} as done.")
    return True