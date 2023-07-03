import datetime

from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.value_objects.status_pedido import StatusPedido
from domain.entities.checkout import Checkout
from domain.entities.fila_atendimento import FilaAtendimento
from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel

class CheckoutService:
    def __init__(self, 
                 checkout_repository: CheckoutRepositoryChannel,
                 pedido_repository: PedidoRepositoryChannel,
                 fila_atendimento_repository: FilaAtendimentoRepositoryChannel) -> None:
        self.checkout_repository  = checkout_repository
        self.pedido_repository = pedido_repository
        self.fila_atendimento_repository = fila_atendimento_repository

    def criar_checkout_para_pedido(self, pedido_id):

        checkout = Checkout(
            id=0,
            pedido_id=pedido_id,
            data_pagamento=datetime.datetime.now(),
            valor_total=150.5,
            created_at=datetime.datetime.now()
        )
        self.checkout_repository.add(checkout)
        self.pedido_repository.update_status(pedido_id, StatusPedido.AGUARDANDO_PREPARO)

        fila = FilaAtendimento(
            id=0,
            pedido_id=pedido_id,
            recebido_em=datetime.datetime.now(),
            finalizado_em= datetime.datetime.now(),
            created_at= datetime.datetime.now(),
        )
        self.fila_atendimento_repository.add(fila)
        return checkout
