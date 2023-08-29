from .entity import Entity
from ..value_objects.cpf import CPF

class Cliente(Entity):
    nome: str
    cpf: CPF
    telefone: str

    def __init__(self, id, nome, cpf, telefone, created_at):
        super().__init__(id, created_at)
        self.nome = nome
        self.cpf = CPF(cpf)
        self.telefone = telefone