
from domain.entities.pedido import Pedido
from domain.value_objects.status_pedido import EmAtendimentoState

class PedidoBuilder:
    def __init__(self):
        self.cliente_id = None
        self.session_id = None
        self.observacoes = None
    
    def com_client_id(self, client_id):
        self.cliente_id = client_id
        return self
    
    def com_session_id(self, session_id):
        self.session_id = session_id
        return self
    
    def com_observacoes(self, observacoes):
        self.observacoes = observacoes
        return self
    
    def build(self)  -> Pedido:
        if not self.cliente_id and not self.session_id:
            raise ValueError("Não se pode iniciar um pedido sem cliente associado ou uma uma sessão associada")

        return Pedido(None, self.cliente_id, self.session_id, self.observacoes, EmAtendimentoState(), None)