from unittest.mock import patch
from floridayvine.persistence import check_database_status


def test_check_database_status_no_connection_string():
    with patch("floridayvine.persistence.mongodb_connection_string", None):
        result, message = check_database_status()
        assert result is False
        assert message == "MONGODB_CONNECTION_STRING environment variable is not set"
