from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from .entity import Entity

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Produto(Entity):
    nome: str
    tamanho: str

    def __init__(self, id, nome, tamanho):
        super().__init__(id)
        self.nome = nome
        self.tamanho = tamanho