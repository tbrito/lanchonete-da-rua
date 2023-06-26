from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from .entity import Entity

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Produto(Entity):
    def __init__(self, id, nome, descricao, categoria_id, created_at):
        super().__init__(id, created_at)
        self.nome = nome
        self.descricao = descricao
        self.categoria_id = categoria_id