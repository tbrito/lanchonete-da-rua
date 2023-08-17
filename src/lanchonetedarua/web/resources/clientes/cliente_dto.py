from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from domain.entities.cliente import Cliente

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ClienteDTO:
    id: int
    nome: str
    cpf: str
    telefone: str

    def __init__(self, cliente: Cliente):
        self.id = cliente.id
        self.nome = cliente.nome
        self.cpf = cliente.cpf.formatado()
        self.telefone = cliente.telefone

    @classmethod
    def from_entity_list(cls, clientes):
        return [cls(cliente) for cliente in clientes]