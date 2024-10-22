"""
Tests for Floriday authentication and API client functionality.
"""

import pytest
from unittest.mock import patch, MagicMock
from floridayvine.floriday.auth import get_access_token, get_auth_info
from floridayvine.floriday.api_client import get_api_client
from requests.exceptions import RequestException


@patch("floridayvine.floriday.auth.requests.request")
def test_get_access_token_success(mock_request):
    mock_response = MagicMock()
    mock_response.json.return_value = {"access_token": "test_token"}
    mock_request.return_value = mock_response

    result = get_access_token()
    assert result == "test_token"


@patch("floridayvine.floriday.auth.requests.request")
def test_get_access_token_failure(mock_request):
    mock_request.side_effect = RequestException("Test error")

    with pytest.raises(RequestException):
        get_access_token()


@patch("floridayvine.floriday.auth.get_access_token")
@patch("floridayvine.floriday.auth.requests.get")
def test_get_auth_info_success(mock_get, mock_get_access_token):
    mock_get_access_token.return_value = "test_token"
    mock_response = MagicMock()
    mock_response.json.return_value = {"key": "value"}
    mock_get.return_value = mock_response

    result = get_auth_info()
    assert result == {"key": "value"}


@patch("floridayvine.floriday.auth.get_access_token")
@patch("floridayvine.floriday.auth.requests.get")
def test_get_auth_info_failure(mock_get, mock_get_access_token):
    mock_get_access_token.return_value = "test_token"
    mock_get.side_effect = RequestException("Test error")

    with pytest.raises(RequestException):
        get_auth_info()


@patch("floridayvine.floriday.api_client.api_factory.ApiFactory")
def test_get_api_client_initial_call(mock_api_factory):
    mock_factory_instance = MagicMock()
    mock_api_client = MagicMock()
    mock_factory_instance.get_api_client.return_value = mock_api_client
    mock_api_factory.return_value = mock_factory_instance

    with patch("floridayvine.floriday.api_client._api_factory", None):
        with patch("floridayvine.floriday.api_client._clt", None):
            result = get_api_client()

    assert result == mock_api_client
    mock_api_factory.assert_called_once()
    mock_factory_instance.get_api_client.assert_called_once()


@patch("floridayvine.floriday.api_client.api_factory.ApiFactory")
def test_get_api_client_subsequent_calls(mock_api_factory):
    mock_factory_instance = MagicMock()
    mock_api_client = MagicMock()
    mock_factory_instance.get_api_client.return_value = mock_api_client
    mock_api_factory.return_value = mock_factory_instance

    with patch("floridayvine.floriday.api_client._api_factory", None):
        with patch("floridayvine.floriday.api_client._clt", None):
            # First call
            result1 = get_api_client()
            assert result1 == mock_api_client
            mock_api_factory.assert_called_once()
            mock_factory_instance.get_api_client.assert_called_once()

            # Reset mock calls
            mock_api_factory.reset_mock()
            mock_factory_instance.get_api_client.reset_mock()

            # Second call
            result2 = get_api_client()
            assert result2 == mock_api_client
            mock_api_factory.assert_not_called()
            mock_factory_instance.get_api_client.assert_not_called()

            # Ensure both calls return the same object
            assert result1 is result2
