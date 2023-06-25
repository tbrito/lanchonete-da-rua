from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from datetime import datetime
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Entity():
    id: int
    created_at: datetime
    
    def __init__(self, id, created_at):
        self.id = id
        self.created_at = created_at