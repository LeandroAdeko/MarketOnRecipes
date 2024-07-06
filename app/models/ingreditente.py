from dataclasses import field, dataclass

@dataclass
class Ingrediente:
    _id: str
    nome: str
    quantidade: float = field(default=0)
    unidade_medida: str = field(default="un")
    preco: float = field(default=0)
    valor_energetico: float = field(default=0)