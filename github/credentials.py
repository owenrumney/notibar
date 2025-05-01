
import keyring
import requests


def save_github_token(token):
    """
    Save the GitHub token to a file.
    """
    try:
        if not token:
            raise ValueError("Token is empty.")
        validate_github_token(token)
        keyring.set_password("notibar", "token", token)
    except ValueError as e:
        print(f"Error saving token: {e}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    

def get_github_token():
    """
    Retrieve the GitHub token from a file.
    """
    try:
        token = keyring.get_password("notibar", "token")
        if token is None:
            raise ValueError("Token not found.")
        return token
    except Exception as e:
        print(f"Error retrieving token: {e}")
        return None
    

def validate_github_token(token):
    """
    Validate the GitHub token.
    """
    if not token:
        raise ValueError("Token is empty.")
    
    # Here you would typically make a request to the GitHub API to validate the token
    # For example, using requests:
    response = requests.get("https://api.github.com/user", headers={"Authorization": f"token {token}"})
    if response.status_code != 200:
        raise ValueError("Invalid token.")
    
    return True