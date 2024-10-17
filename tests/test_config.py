import pytest
from unittest.mock import patch
import os
from floridayvine.config import check_environment_variables


@pytest.fixture
def mock_env_vars():
    with patch.dict(
        os.environ,
        {
            "FLORIDAY_CLIENT_ID": "test_id",
            "FLORIDAY_CLIENT_SECRET": "test_secret",
            "FLORIDAY_AUTH_URL": "http://test.auth.url",
            "FLORIDAY_BASE_URL": "http://test.base.url",
            "FLORIDAY_API_KEY": "test_api_key",
            "MONGODB_CONNECTION_STRING": "test_connection_string",
        },
    ):
        yield


def test_check_environment_variables_all_set(mock_env_vars):
    # This should not raise any exception or exit the system
    check_environment_variables()


def test_check_environment_variables_missing():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(SystemExit) as exc_info:
            check_environment_variables()
        assert exc_info.value.code == 1


def test_check_environment_variables_partial_missing():
    with patch.dict(
        os.environ,
        {"FLORIDAY_CLIENT_ID": "test_id", "FLORIDAY_CLIENT_SECRET": "test_secret"},
        clear=True,
    ):
        with pytest.raises(SystemExit) as exc_info:
            check_environment_variables()
        assert exc_info.value.code == 1


@patch("builtins.print")
def test_check_environment_variables_error_message(mock_print):
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(SystemExit):
            check_environment_variables()

    mock_print.assert_any_call(
        "Error: Missing required environment variables: FLORIDAY_CLIENT_ID, FLORIDAY_CLIENT_SECRET, FLORIDAY_AUTH_URL, FLORIDAY_BASE_URL, FLORIDAY_API_KEY, MONGODB_CONNECTION_STRING"
    )
    mock_print.assert_any_call(
        "Please set these variables before running the application."
    )
    mock_print.assert_any_call(
        "For more information, refer to the project documentation:"
    )
    mock_print.assert_any_call(
        "https://github.com/serraict/vine-floriday-adapter#readme"
    )
