from pymongo import MongoClient


def persist(collection: str, _id: str, data: dict):
    """
    Persist data to the database.
    """
    # Using the 'with' statement for MongoDB client to ensure proper resource management
    with MongoClient("mongodb://localhost:27017/") as client:
        # Access the 'floriday' database
        db = client["floriday"]

        # Access the specified collection
        coll = db[collection]

        # Insert or update the document in the collection
        coll.update_one({"_id": _id}, {"$set": data}, upsert=True)
