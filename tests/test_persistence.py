from unittest.mock import patch, MagicMock, call
from floridayvine.persistence import (
    check_database_status,
    DATABASE,
    SYNC_COLLECTIONS,
    initialize_database,
)


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


def test_initialize_database_no_connection_string():
    with patch("floridayvine.persistence.mongodb_connection_string", None):
        with patch("builtins.print") as mock_print:
            initialize_database()
            mock_print.assert_called_once_with(
                "Error: MONGODB_CONNECTION_STRING environment variable is not set"
            )


def test_initialize_database_success():
    mock_client = MagicMock()
    mock_db = mock_client[DATABASE]
    mock_db.list_collection_names.return_value = [
        SYNC_COLLECTIONS[0]
    ]  # Assume one collection already exists

    with (
        patch(
            "floridayvine.persistence.mongodb_connection_string",
            "mock_connection_string",
        ),
        patch(
            "floridayvine.persistence.masked_connection_string",
            "mongodb://user:'*****'@host:port",
        ),
        patch("floridayvine.persistence.MongoClient") as mock_mongo_client,
        patch("builtins.print") as mock_print,
    ):
        mock_mongo_client.return_value.__enter__.return_value = mock_client
        initialize_database()

        # Check if collections are created only if they don't exist
        assert mock_db.create_collection.call_count == len(SYNC_COLLECTIONS) - 1
        mock_db.create_collection.assert_has_calls(
            [call(name) for name in SYNC_COLLECTIONS[1:]]
        )

        # Check if index is created for all collections
        expected_index_calls = [
            call([("sequence_number", -1)]) for _ in SYNC_COLLECTIONS
        ]
        for collection_name in SYNC_COLLECTIONS:
            mock_collection = mock_db[collection_name]
            mock_collection.create_index.assert_has_calls(
                expected_index_calls, any_order=True
            )

        # Check print statements
        mock_print.assert_any_call(
            "Initializing database on mongodb://user:'*****'@host:port..."
        )
        for collection_name in SYNC_COLLECTIONS[1:]:
            mock_print.assert_any_call(f"Created collection: {collection_name}")
        mock_print.assert_called_with("Database initialization complete.")
