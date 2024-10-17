from unittest.mock import patch, MagicMock
from floridayvine.persistence import check_database_status, DATABASE, SYNC_COLLECTIONS


def test_check_database_status_no_connection_string():
    with patch("floridayvine.persistence.mongodb_connection_string", None):
        result, message = check_database_status()
        assert result is False
        assert message == "MONGODB_CONNECTION_STRING environment variable is not set"


def test_check_database_status_database_not_exist():
    mock_client = MagicMock()
    mock_client.list_database_names.return_value = []
    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.MongoClient") as mock_mongo_client:
            mock_mongo_client.return_value.__enter__.return_value = mock_client
            result, message = check_database_status()
            assert result is False
            assert message == "Database does not exist"
            mock_client.list_database_names.assert_called_once()


def test_check_database_status_missing_collection():
    mock_client = MagicMock()
    mock_client.list_database_names.return_value = [DATABASE]
    mock_db = mock_client[DATABASE]
    mock_db.list_collection_names.return_value = SYNC_COLLECTIONS[1:]

    with (
        patch(
            "floridayvine.persistence.mongodb_connection_string",
            "mock_connection_string",
        ),
        patch("floridayvine.persistence.MongoClient") as mock_mongo_client,
    ):
        mock_mongo_client.return_value.__enter__.return_value = mock_client
        result, message = check_database_status()

        assert result is False
        assert message == f"Collection {SYNC_COLLECTIONS[0]} does not exist"
        mock_client.list_database_names.assert_called_once()
        mock_db.list_collection_names.assert_called_once()
