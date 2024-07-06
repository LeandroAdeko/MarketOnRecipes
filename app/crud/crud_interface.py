from app.db.session import MongoDBSessionManager
from app.errors.mongo_errors import error_handler

from typing import Any, Dict, List, Optional

class CRUDInterface:

    def __init__(self, collection_name: str) -> None:
        self.collection_name = collection_name
    
    @error_handler
    def set_unique_keys(self, keys: list[str], value: True):
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            for key in keys:
                collection.create_index(key, unique=value)
    
    @error_handler
    def create(self, data: Dict[str, Any]):
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            inset_response = collection.insert_one(data)
        return inset_response

    @error_handler
    def read(self, filter: dict[str]) -> Optional[List]:
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            document = list(collection.find(filter))
        return document

    @error_handler
    def update_one(self, data: Dict[str, Any]):
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            update_response = collection.replace_one({'_id': data['_id']}, data)
        return update_response

    @error_handler
    def delete(self, entity_id: str):
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            delete_response = collection.delete_one({"_id": entity_id})
        return delete_response

    @error_handler
    def list_all(self) -> List[Dict]:
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            all_documents = collection.find()

        return list(all_documents)
