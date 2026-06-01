from unittest.mock import patch, MagicMock
from floridayvine.commands.about import check_api_version


@patch("floridayvine.commands.about.get_api_client")
def test_check_api_version_success(mock_get_api_client):
    """Test that check_api_version returns None when the API version is correct."""
    # Mock the get_api_client function to return without raising an exception
    mock_get_api_client.return_value = MagicMock()

    # Call the function
    result = check_api_version()

    # Verify the result
    assert result is None
    mock_get_api_client.assert_called_once()


@patch("floridayvine.commands.about.get_api_client")
def test_check_api_version_failure(mock_get_api_client):
    """Test that check_api_version returns an error message when the API version is incorrect."""
    # Mock the get_api_client function to raise a ValueError
    error_message = "API version mismatch. Base URL points to version 2024v1 but this client was generated for version 2024v2."
    mock_get_api_client.side_effect = ValueError(error_message)

    # Call the function
    result = check_api_version()

    # Verify the result
    assert result == error_message
    mock_get_api_client.assert_called_once()


@patch("floridayvine.commands.about.get_api_client")
def test_check_api_version_ignores_auth_errors(mock_get_api_client):
    """Auth/network failures must not crash `about`; they are reported elsewhere.

    ApiFactory authenticates eagerly in its constructor, so get_api_client can
    raise non-ValueError errors (e.g. HTTPError) when credentials are missing.
    check_api_version should swallow those and return None.
    """
    mock_get_api_client.side_effect = RuntimeError("400 Client Error: Bad Request")

    result = check_api_version()

    assert result is None
    mock_get_api_client.assert_called_once()
