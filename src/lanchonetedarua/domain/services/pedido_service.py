from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel


class PedidoService:

    def __init__(self, pedido_repository: PedidoRepositoryChannel) -> None:
        self.pedido_repository  = pedido_repository
 
    def obter_pedidos(self):
        return self.pedido_repository.get_all()
        
    def criar_pedido(self, pedido_data):
        self.pedido_repository.add(pedido_data)

    def obter_pedido_por_id(self, pedido_id):
        return self.pedido_repository.get_by_id(pedido_id)
    
    def atualizar_pedido(self, pedido_id, pedido_data):
        self.pedido_repository.update(pedido_id, pedido_data)

    def deletar_pedido(self, pedido_id):
        self.pedido_repository.delete(pedido_id)