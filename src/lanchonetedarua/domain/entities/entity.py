from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Entity():
    id: int
    def __init__(self, id):
        self.id = id