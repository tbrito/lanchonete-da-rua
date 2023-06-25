
from .entity import Entity

class Pedido(Entity):
    def __init__(self, id, cliente_id, itens, observacoes, status, created_at):
        super().__init__(id, created_at)
        self.cliente_id = cliente_id
        self.itens = itens
        self.observacoes = observacoes
        self.status = status

    def altera_status(self, status):
        self.status = status