from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from .entity import Entity

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Categoria(Entity):
    def __init__(self, id, nome, created_at):
        super().__init__(id, created_at)
        self.nome = nome