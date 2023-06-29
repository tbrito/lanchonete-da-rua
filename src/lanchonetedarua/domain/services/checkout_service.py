from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.value_objects.status_pedido import StatusPedido

class CheckoutService:
    def __init__(self, 
                 checkout_repository: CheckoutRepositoryChannel,
                 pedido_repository: PedidoRepositoryChannel) -> None:
        self.checkout_repository  = checkout_repository
        self.pedido_repository = pedido_repository

    def criar_checkout_para_pedido(self, checkout):
        self.pedido_repository.update_status(checkout.pedido_id, "AGUARDANDO_PREPARO")
        self.checkout_repository.add(checkout)
