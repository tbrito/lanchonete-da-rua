from datetime import datetime
from .entity import Entity
from domain.value_objects.status_pagamento import StatusPagamento

class Checkout(Entity):
    pedido_id: int
    valor_total: float
    data_pagamento: datetime = None
    status_pagamento: StatusPagamento = None

    def __init__(self, id, pedido_id, valor_total, created_at):
        super().__init__(id, created_at)
        self.pedido_id = pedido_id
        self.valor_total = valor_total