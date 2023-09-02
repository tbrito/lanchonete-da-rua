from typing import Type
from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.repositories.item_pedido_repository_channel import ItemPedidoRepositoryChannel
from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel
from domain.builders.pedido_builder import PedidoBuilder
from domain.entities.pedido import Pedido
from web.resources.pedidos.pedido_input import PedidoInput
from domain.value_objects.status_pedido import FinalizadoState

class PedidoService:

    def __init__(
            self, 
            pedido_repository: PedidoRepositoryChannel, 
            item_pedido_repository: ItemPedidoRepositoryChannel,
            fila_atendimento_repository: FilaAtendimentoRepositoryChannel) -> Type['PedidoService']:
        self.pedido_repository  = pedido_repository
        self.item_pedido_repository  = item_pedido_repository
        self.fila_atendimento_repository = fila_atendimento_repository
        
    def obter_pedidos(self):
        return self.pedido_repository.obter_todos_os_pedidos()
 
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
        pedido = self.pedido_repository.update(pedido_id, pedido_data)
        
        if isinstance(pedido.status, FinalizadoState):
            self.fila_atendimento_repository.finalizar_by_pedido_id(pedido_id)

        return pedido
        
    def atualizar_status(self, pedido_id, status):
        self.pedido_repository.update_status(pedido_id, status)

    def deletar_pedido(self, pedido_id):
        self.pedido_repository.delete(pedido_id)

    def adicionar_item_pedido(self, pedido_id, _item_pedido):
        return self.item_pedido_repository.add(pedido_id, _item_pedido)

    def editar_item_pedido(self, pedido_id, item_pedido_id, _item_pedido):
        self.item_pedido_repository.update(pedido_id, item_pedido_id, _item_pedido)

    def obter_item_pedido_por_id(self, item_pedido_id):
        self.item_pedido_repository.get_by_id(item_pedido_id)

    def deletar_item_pedido(self, item_pedido_id):
       self.item_pedido_repository.delete(item_pedido_id)