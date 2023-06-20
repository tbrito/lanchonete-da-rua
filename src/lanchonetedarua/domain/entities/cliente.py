from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from .entity import Entity

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Cliente(Entity):
    nome: str
    cpf: str
    telefone: str

    def __init__(self, id, nome, cpf, telefone):
        super().__init__(id)
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone