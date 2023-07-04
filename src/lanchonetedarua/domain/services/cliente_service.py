from typing import List

from domain.repositories.cliente_repository_channel import ClienteRepositoryChannel
from domain.builders.cliente_builder import ClienteBuilder

from domain.entities.cliente import Cliente


class ClienteService:

    def __init__(self, cliente_repository: ClienteRepositoryChannel) -> None:
        self.cliente_repository  = cliente_repository
 
    def obter_clientes(self) -> List[Cliente]:
        return self.cliente_repository.get_all()
        
    def criar_cliente(self, cliente_data) -> Cliente:
        cliente = ClienteBuilder().com_nome(cliente_data.nome).com_cpf(cliente_data.cpf).com_telefone(cliente_data.telefone).build()
        return self.cliente_repository.add(cliente)

    def obter_cliente_por_id(self, cliente_id) -> Cliente:
        return self.cliente_repository.get_by_id(cliente_id)

    def obter_cliente_por_cpf(self, cliente_cpf) -> Cliente:
        return self.cliente_repository.get_by_cpf(cliente_cpf)
    
    def atualizar_cliente(self, cliente_id, cliente_data) -> Cliente:
        return self.cliente_repository.update(cliente_id, cliente_data)

    def deletar_cliente(self, cliente_id):
        self.cliente_repository.delete(cliente_id)