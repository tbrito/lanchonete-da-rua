import inject
from domain.entities.cliente import Cliente
from domain.repositories.cliente_repository_channel import ClienteRepositoryChannel

class ClienteService:

    @inject.autoparams()
    def __init__(self, usuario_repository: ClienteRepositoryChannel) -> None:
        self.usuario_repository  = usuario_repository
 
    def obter_clientes(self):
        return self.usuario_repository.get_all()
        
    def criar_cliente(self, cliente_data):
        self.usuario_repository.add(cliente_data)

    def obter_cliente_por_id(self, cliente_id):
        return self.usuario_repository.get_by_id(cliente_id)

    def obter_cliente_por_cpf(self, cliente_cpf):
        return self.get_by_cpf(cliente_cpf)
    
    def atualizar_cliente(self, cliente_id, cliente_data):
        self.usuario_repository.update(cliente_id, cliente_data)

    def deletar_cliente(self, cliente_id):
        self.usuario_repository.v(cliente_id)