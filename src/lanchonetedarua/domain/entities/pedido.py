from domain.value_objects.status_pedido import EmAtendimentoState, FinalizadoParaPagamentoState, PedidoAbandonadoState, StatusPedido
from .entity import Entity

class Pedido(Entity):
    cliente_id: int
    session_id: int
    observacoes: str
    status: StatusPedido
    def __init__(self, id, cliente_id, session_id, observacoes, status, created_at):
        super().__init__(id, created_at)
        self.cliente_id = cliente_id
        self.session_id = session_id
        self.observacoes = observacoes
        self.status = status

    def avancar_status(self):
        self.status.avancar(self)
    
    def retroceder_status(self):
        self.status.retroceder(self)
    
    def mostrar_estado(self):
        print(f"Estado atual: {self.status.nome}")
        
    def desistir(self):
        if isinstance(self.status, EmAtendimentoState) or isinstance(self.status, FinalizadoParaPagamentoState):
            self.status = PedidoAbandonadoState()
            print("Pedido abandonado.")
        else:
            print("Não é possível desistir neste estado.")