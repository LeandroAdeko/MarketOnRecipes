from dataclasses import field, dataclass

@dataclass
class Pessoa:
    _id: str
    nome: str
    energia_necessaria: float = field(default=0)