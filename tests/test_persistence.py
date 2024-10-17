from unittest.mock import patch, MagicMock, call
from floridayvine.persistence import (
    check_database_status,
    DATABASE,
    SYNC_COLLECTIONS,
    initialize_database,
    get_max_sequence_number,
    print_sync_status,
    persist,
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


def test_get_max_sequence_number_empty_collection():
    mock_client = MagicMock()
    mock_db = mock_client[DATABASE]
    mock_collection = mock_db["test_collection"]
    mock_collection.find_one.return_value = None

    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.MongoClient") as mock_mongo_client:
            mock_mongo_client.return_value.__enter__.return_value = mock_client
            with patch("builtins.print") as mock_print:
                result = get_max_sequence_number("test_collection")
                assert result == 0
                mock_print.assert_called_once_with(
                    "No sequence number found for collection test_collection."
                )


def test_get_max_sequence_number_with_documents():
    mock_client = MagicMock()
    mock_db = mock_client[DATABASE]
    mock_collection = mock_db["test_collection"]
    mock_collection.find_one.return_value = {"sequence_number": 42}

    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.MongoClient") as mock_mongo_client:
            mock_mongo_client.return_value.__enter__.return_value = mock_client
            result = get_max_sequence_number("test_collection")
            assert result == 42
            mock_collection.find_one.assert_called_once_with(
                {}, sort=[("sequence_number", -1)]
            )


def test_print_sync_status_no_connection_string():
    with patch("floridayvine.persistence.mongodb_connection_string", None):
        with patch("builtins.print") as mock_print:
            print_sync_status()
            mock_print.assert_called_once_with(
                "Error: MONGODB_CONNECTION_STRING environment variable is not set"
            )


def test_print_sync_status_with_sequence_numbers():
    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.get_max_sequence_number") as mock_get_max:
            mock_get_max.side_effect = [10, 20, 30]
            with patch("builtins.print") as mock_print:
                print_sync_status()
                mock_print.assert_has_calls(
                    [
                        call(f"Max sequence number for {SYNC_COLLECTIONS[0]}: 10"),
                        call(f"Max sequence number for {SYNC_COLLECTIONS[1]}: 20"),
                        call(f"Max sequence number for {SYNC_COLLECTIONS[2]}: 30"),
                    ]
                )


def test_print_sync_status_some_collections_empty():
    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.get_max_sequence_number") as mock_get_max:
            mock_get_max.side_effect = [10, 0, 30]
            with patch("builtins.print") as mock_print:
                print_sync_status()
                mock_print.assert_has_calls(
                    [
                        call(f"Max sequence number for {SYNC_COLLECTIONS[0]}: 10"),
                        call(f"Max sequence number for {SYNC_COLLECTIONS[1]}: 0"),
                        call(f"Max sequence number for {SYNC_COLLECTIONS[2]}: 30"),
                    ]
                )


def test_persist_no_connection_string():
    with patch("floridayvine.persistence.mongodb_connection_string", None):
        with patch("builtins.print") as mock_print:
            persist("test_collection", "test_id", {"key": "value"})
            mock_print.assert_called_once_with(
                "Error: MONGODB_CONNECTION_STRING environment variable is not set"
            )


def test_persist_insert():
    mock_client = MagicMock()
    mock_db = mock_client[DATABASE]
    mock_collection = mock_db["test_collection"]

    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.MongoClient") as mock_mongo_client:
            mock_mongo_client.return_value.__enter__.return_value = mock_client
            persist("test_collection", "test_id", {"key": "value"})
            mock_collection.update_one.assert_called_once_with(
                {"_id": "test_id"}, {"$set": {"key": "value"}}, upsert=True
            )


def test_persist_update():
    mock_client = MagicMock()
    mock_db = mock_client[DATABASE]
    mock_collection = mock_db["test_collection"]

    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.MongoClient") as mock_mongo_client:
            mock_mongo_client.return_value.__enter__.return_value = mock_client
            persist("test_collection", "existing_id", {"key": "updated_value"})
            mock_collection.update_one.assert_called_once_with(
                {"_id": "existing_id"}, {"$set": {"key": "updated_value"}}, upsert=True
            )


def test_persist_different_collections():
    mock_client = MagicMock()
    mock_db = mock_client[DATABASE]

    with patch(
        "floridayvine.persistence.mongodb_connection_string", "mock_connection_string"
    ):
        with patch("floridayvine.persistence.MongoClient") as mock_mongo_client:
            mock_mongo_client.return_value.__enter__.return_value = mock_client
            for collection_name in SYNC_COLLECTIONS:
                persist(
                    collection_name, f"{collection_name}_id", {"key": collection_name}
                )
                mock_db[collection_name].update_one.assert_called_with(
                    {"_id": f"{collection_name}_id"},
                    {"$set": {"key": collection_name}},
                    upsert=True,
                )
