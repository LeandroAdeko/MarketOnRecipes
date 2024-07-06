from app.crud.crud_interface import CRUDInterface
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

    def read(self, filter: dict[str]) -> List[UnidadeMedida]:
        documents = super().read(filter)

        un_list: list[UnidadeMedida] = []
        for document in documents:
            un_list.append(UnidadeMedida(**document))
        return un_list

    def update_one(self, data: Dict[str, Any]) -> Optional[Any]:
        update_response = super().update_one(data)
        return update_response

    def delete(self, entity_id: str) -> bool: ## Revise
        delete_response = super().delete(entity_id)
        return delete_response

    def list_all(self) -> List[Any]:
        all_documents = super().list_all()
        return all_documents