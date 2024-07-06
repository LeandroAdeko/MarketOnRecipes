from dataclasses import field, dataclass

@dataclass
class Receita:
    _id: str
    ingredientes: list[dict[str]] # [{"ingrediente_id": _id, "quantidade": 999, "unidade_medida": "un"}]
    descricao: str

