from domain.repositories.cliente_repository_channel import ClienteRepositoryChannel
from domain.entities.cliente import Cliente
# from adapters.mappings import cliente_map

class ClienteRepository(ClienteRepositoryChannel):
    def get_by_id(self, cliente_id):
        return ""
     
    def get_all(self):
      
        return Cliente.query.all()

    def get_by_cpf(self, cliente_cpf):
        return "obter cpf do repositorio"    

    def add(self, cliente):
        ... 

    def update(self, cliente_id, cliente):
        return "atualizar cliente no repositorio"    

    def delete(self, cliente_id):
        return "excluir um cliente do repositorio"    