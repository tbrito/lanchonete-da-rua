
from typing import Type
from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.repositories.item_pedido_repository_channel import ItemPedidoRepositoryChannel
from domain.builders.pedido_builder import PedidoBuilder
from domain.entities.pedido import Pedido
from web.resources.pedidos.pedido_input import PedidoInput

class PedidoService:

    def __init__(
            self, 
            pedido_repository: PedidoRepositoryChannel, 
            item_pedido_repository: ItemPedidoRepositoryChannel) -> Type['PedidoService']:
        self.pedido_repository  = pedido_repository
        self.item_pedido_repository  = item_pedido_repository
 
    def obter_pedidos_nao_finalizados(self):
        return self.pedido_repository.obter_pedidos_nao_finalizados()
        
    def criar_pedido(self, pedido_data: PedidoInput):
        pedido_entity = ( 
                         PedidoBuilder()
                         .com_client_id(pedido_data.cliente_id)
                         .com_session_id(pedido_data.session_id)
                         .com_observacoes(pedido_data.observacoes)
                         .build())
        
        self.pedido_repository.add(pedido_entity)

    def obter_pedido_por_id(self, pedido_id) -> Pedido:
        return self.pedido_repository.get_by_id(pedido_id) 
    
    def atualizar_pedido(self, pedido_id: int, pedido_data: Pedido):
        return self.pedido_repository.update(pedido_id, pedido_data)
        
    def atualizar_status(self, pedido_id, status):
        self.pedido_repository.update_status(pedido_id, status)

    def deletar_pedido(self, pedido_id):
        self.pedido_repository.delete(pedido_id)

    def adicionar_item_pedido(self, pedido_id, _item_pedido):
        self.item_pedido_repository.add(pedido_id, _item_pedido)

    def editar_item_pedido(self, pedido_id, item_pedido_id, _item_pedido):
        self.item_pedido_repository.update(pedido_id, item_pedido_id, _item_pedido)

    def obter_item_pedido_por_id(self, item_pedido_id):
        self.item_pedido_repository.get_by_id(self, item_pedido_id)

    def deletar_item_pedido(self, item_pedido_id):
       self.item_pedido_repository.delete(item_pedido_id)