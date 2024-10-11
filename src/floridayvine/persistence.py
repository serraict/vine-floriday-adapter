import os
from pymongo import MongoClient
import re

mongodb_connection_string = os.getenv("MONGODB_CONNECTION_STRING")

# Regular expression pattern to match and mask the password
pattern = r"(mongodb://[^:]+:)([^@]+)(@.+)"
masked_connection_string = re.sub(pattern, r"\1'*****'\3", mongodb_connection_string)

DATABASE = "floriday"
SYNC_COLLECTIONS = ["organizations", "trade_items"]


def check_database_status():
    with MongoClient(mongodb_connection_string) as client:
        # Check if the database exists
        db_names = client.list_database_names()
        db_exists = DATABASE in db_names

        if not db_exists:
            return False, "Database does not exist"

        db = client[DATABASE]

        # Check if required collections exist and have the necessary index
        for collection_name in SYNC_COLLECTIONS:
            if collection_name not in db.list_collection_names():
                return False, f"Collection {collection_name} does not exist"

            collection = db[collection_name]
            indices = collection.index_information()
            if "sequence_number_-1" not in indices:
                return False, f"Required index missing in {collection_name}"

        return True, "Database and indices are properly set up"


def initialize_database():
    """
    Initialize the database.
    """
    print(f"Initializing database on {masked_connection_string}...")
    with MongoClient(mongodb_connection_string) as client:
        db = client[DATABASE]
        existing_collections = set(db.list_collection_names())
        for collection_name in SYNC_COLLECTIONS:
            if collection_name not in existing_collections:
                db.create_collection(collection_name)
                print(f"Created collection: {collection_name}")
            collection = db[collection_name]
            # Create a descending index on the sequence_number field so that we can easily
            # retrieve the maximum sequence number for a collection to use as the base of
            # the synchronization process.
            collection.create_index([("sequence_number", -1)])
        print("Database initialization complete.")


def get_max_sequence_number(collection_name: str):
    with MongoClient(mongodb_connection_string) as client:
        db = client[DATABASE]
        collection = db[collection_name]
        max_sequence_number_doc = collection.find_one(
            {}, sort=[("sequence_number", -1)]
        )

        if max_sequence_number_doc:
            max_sequence_number = max_sequence_number_doc["sequence_number"]
        else:
            max_sequence_number = 0

        return max_sequence_number


def print_sync_status():
    for collection_name in SYNC_COLLECTIONS:
        max_sequence_number = get_max_sequence_number(collection_name)
        print(f"Max sequence number for {collection_name}: {max_sequence_number}")


def persist(collection: str, _id: str, data: dict):
    with MongoClient(mongodb_connection_string) as client:
        db = client[DATABASE]
        coll = db[collection]
        coll.update_one({"_id": _id}, {"$set": data}, upsert=True)
