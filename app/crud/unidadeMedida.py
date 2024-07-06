from app.crud.crud_interface import CRUDInterface
from app.db.session import MongoDBSessionManager
from app.models.unidadeMedida import UnidadeMedida

from typing import Any, Dict, List, Optional



class CRUDUnidadeMedida(CRUDInterface):

    unique_keys = ["nome", "abreviacao"]
    def __init__(self) -> None:
        super().__init__("UnidadeMedida")
        self.set_unique_keys()
    
    def set_unique_keys(self):
        return super().set_unique_keys(self.unique_keys, True)
    
    def create(self, data: Dict[str, Any]) -> Any:
        inset_response = super().create(data)
        print(inset_response)

    def read(self, entity_id: str) -> List[UnidadeMedida]:
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            documents = list(collection.find({"_id": entity_id}))

        un_list: list[UnidadeMedida] = []
        for document in documents:
            un_list.append(UnidadeMedida(**document))
        return un_list

    def update(self, data: Dict[str, Any]) -> Optional[Any]:
        update_response = super().update(data)
        return update_response

    def delete(self, entity_id: str) -> bool:
        delete_response = super().delete(entity_id)
        with MongoDBSessionManager() as db:
            collection = db.get_collection(self.collection_name)
            delete_response = collection.delete_one({"_id": entity_id})
        return delete_response

    def list_all(self) -> List[Any]:
        all_documents = super().list_all()
        return all_documents