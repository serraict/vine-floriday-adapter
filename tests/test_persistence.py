from unittest.mock import patch, MagicMock
from floridayvine.persistence import check_database_status


def test_check_database_status_no_connection_string():
    with patch("floridayvine.persistence.mongodb_connection_string", None):
        result, message = check_database_status()
        assert result is False
        assert message == "MONGODB_CONNECTION_STRING environment variable is not set"


def test_check_database_status_database_not_exist():
    mock_client = MagicMock()
    mock_client.list_database_names.return_value = []
    with patch("floridayvine.persistence.MongoClient", return_value=mock_client):
        result, message = check_database_status()
        assert result is False
        assert message == "Database does not exist"
