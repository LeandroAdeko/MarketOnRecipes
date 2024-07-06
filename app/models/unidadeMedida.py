from dataclasses import dataclass


@dataclass
class UnidadeMedida:
    _id: str
    nome: str
    abreviacao: str


# UNIDADE = UnidadeMedida('Unidade', 'un')
# KILO = UnidadeMedida('Kilo', 'Kg')
# GRAMA = UnidadeMedida('Grama', 'g')
# LITRO = UnidadeMedida('Litro', 'L')
# MILILITRO = UnidadeMedida('Mililitro', 'mL')
# CAIXA = UnidadeMedida('Caixa', 'cx')
# COLHER_SOPA = UnidadeMedida('Colher de sopa', 'colher sopa')
# COLHER_CHA = UnidadeMedida('Colher de chá', 'colher chá')