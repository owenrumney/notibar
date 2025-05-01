import pytest
from github.credentials import save_github_token, get_github_token

def test_save_github_token(mocker):
    # Mock keyring.set_password
    mock_set = mocker.patch('keyring.set_password')
    
    # Test saving a token
    test_token = "test-token-123"
    save_github_token(test_token)
    
    # Verify keyring.set_password was called with correct arguments
    mock_set.assert_called_once_with("notibar", "token", test_token)

def test_get_github_token_success(mocker):
    # Mock keyring.get_password to return a token
    mock_get = mocker.patch('keyring.get_password', return_value="test-token-123")
    
    # Test retrieving the token
    token = get_github_token()
    
    assert token == "test-token-123"
    mock_get.assert_called_once_with("notibar", "token")

def test_get_github_token_not_found(mocker):
    # Mock keyring.get_password to return None
    mocker.patch('keyring.get_password', return_value=None)
    
    # Test retrieving when token doesn't exist
    token = get_github_token()
    
    assert token is None

def test_get_github_token_error(mocker):
    # Mock keyring.get_password to raise an exception
    mocker.patch('keyring.get_password', side_effect=Exception("Test error"))
    
    # Test retrieving when there's an error
    token = get_github_token()
    
    assert token is None