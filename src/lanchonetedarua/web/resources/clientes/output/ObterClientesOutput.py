from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ObterClientesOutput:
    id : int
    nome : str
    cpf : str
    telefone : str
    created_at : datetime
    def __init__(self, id, nome, cpf, telefone, created_at):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.created_at = created_at

