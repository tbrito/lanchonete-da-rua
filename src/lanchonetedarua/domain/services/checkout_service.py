import datetime

from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.entities.checkout import Checkout
from domain.entities.fila_atendimento import FilaAtendimento
from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel
from domain.repositories.item_pedido_repository_channel import ItemPedidoRepositoryChannel
from domain.value_objects.status_pedido import FinalizadoParaPagamentoState


class CheckoutService:
    def __init__(self, 
                 checkout_repository: CheckoutRepositoryChannel,
                 pedido_repository: PedidoRepositoryChannel,
                 fila_atendimento_repository: FilaAtendimentoRepositoryChannel,
                 item_pedido_repository : ItemPedidoRepositoryChannel
                 ) -> None:
        self.checkout_repository  = checkout_repository
        self.pedido_repository = pedido_repository
        self.fila_atendimento_repository = fila_atendimento_repository
        self.item_pedido_repository = item_pedido_repository

    def criar_checkout_para_pedido(self, pedido_id):
        itens = self.item_pedido_repository.get_by_pedido_id(pedido_id)
        valor_total = sum(item.valor for item in itens)
        checkout = Checkout(
            id=0,
            pedido_id=pedido_id,
            data_pagamento=datetime.datetime.now(),
            valor_total=valor_total,
            created_at=datetime.datetime.now()
        )
        pedido = self.pedido_repository.get_by_id(pedido_id)
        if not isinstance(pedido.status, FinalizadoParaPagamentoState):
            return f"Não é possível realizar o checkout de um pedido com o estado {pedido.status}"; 
            
        self.checkout_repository.add(checkout)
        pedido.status.avancar(pedido)
        
        self.pedido_repository.update(pedido_id, pedido)

        fila = FilaAtendimento(
            id=0,
            pedido_id=pedido_id,
            recebido_em=datetime.datetime.now(),
            finalizado_em= datetime.datetime.now(),
            created_at= datetime.datetime.now(),
        )
        self.fila_atendimento_repository.add(fila)
        return checkout
