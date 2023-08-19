from .entity import Entity

class Pedido(Entity):
    cliente_id: int
    session_id: int
    observacoes: str
    status: str
    
    def __init__(self, id, cliente_id, session_id, observacoes, status, created_at):
        super().__init__(id, created_at)
        self.cliente_id = cliente_id
        self.session_id = session_id
        self.observacoes = observacoes
        self.status = status.name

    def altera_status(self, status):
        self.status = status