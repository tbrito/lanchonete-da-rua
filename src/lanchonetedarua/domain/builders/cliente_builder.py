from domain.value_objects.cpf import CPF
from domain.entities.cliente import Cliente

class ClienteBuilder:
    def __init__(self):
        self.nome = None
        self.cpf = None
        self.telefone = None

    def com_nome(self, nome):
        self.nome = nome
        return self

    def com_cpf(self, cpf):
        self.cpf = cpf
        return self

    def com_telefone(self, telefone):
        self.telefone = telefone
        return self

    def build(self):
        if not self.nome:
            raise ValueError("É necessário informar o nome do cliente")
        return Cliente(None, self.nome, self.cpf, self.telefone, None)