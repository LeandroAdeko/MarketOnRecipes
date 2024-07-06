from pymongo import MongoClient
from typing import Optional
from dotenv import load_dotenv
import logging
import os

load_dotenv()

class MongoDBSession:
    _client: Optional[MongoClient] = None
    _connection_string: str = os.getenv("MONGO_CONNECTION_STRING", None)
    _database_name: str = os.getenv("MONGO_DATABASE_NAME", None)

    def __init__(self):
        self._client = None

    def connect(self):
        if self._client is None:
            logging.debug("Connecting to MongoDB")
            self._client = MongoClient(self._connection_string)
        return self._client

    def get_database(self):
        if self._client is None:
            raise Exception("Client is not connected")
        logging.debug(f"Getting database: {self._database_name}")
        return self._client[self._database_name]

    def close(self):
        if self._client:
            logging.debug("Closing MongoDB connection")
            self._client.close()
            self._client = None

# Context manager for database session
class MongoDBSessionManager:
    def __init__(self):
        self.session = MongoDBSession()

    def __enter__(self):
        self.session.connect()
        return self.session.get_database()

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()


# from app.db.session import MongoDBSessionManager

# def create_user(user_data):
#     with MongoDBSessionManager() as db:
#         users_collection = db.get_collection("users")
#         users_collection.insert_one(user_data)

# def list_users():
#     with MongoDBSessionManager() as db:
#         users_collection = db.get_collection("users")
#         return list(users_collection.find())