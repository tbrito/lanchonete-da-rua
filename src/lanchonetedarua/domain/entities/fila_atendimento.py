from datetime import datetime
from .entity import Entity

class FilaAtendimento(Entity):
    pedido_id: int
    recebido_em: datetime
    finalizado_em: datetime
    
    def __init__(self, id, pedido_id, recebido_em, created_at, finalizado_em=None):
        super().__init__(id, created_at)
        self.pedido_id = pedido_id
        self.recebido_em = recebido_em
        self.finalizado_em = finalizado_em
