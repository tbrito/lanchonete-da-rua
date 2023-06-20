
from value_objects.status_pedido import StatusPedido
from .entity import Entity

class Pedido(Entity):
    def __init__(self, id, cliente, itens, observacoes):
        super().__init__(id)
        self.cliente = cliente
        self.itens = itens
        self.observacoes = observacoes
        self.status = StatusPedido.EM_ATENDIMENTO

    def altera_status(self, status):
        self.status = status