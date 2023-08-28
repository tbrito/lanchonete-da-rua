class StatusPedido:
    def avancar(self, pedido):
        pass
    
    def retroceder(self, pedido):
        pass
    
    def desistir(self, pedido):
        pass
    
    @staticmethod
    def get_status_from_database(status_string):
        if status_string in status_mapping:
            status_instance = status_mapping[status_string]
            return status_instance
        else:
            raise("Unknown status:", status_string)


class EmAtendimentoState(StatusPedido):
    def __init__(self):
        self.nome = "Em Atendimento"
        
    def avancar(self, pedido):
        pedido.status = FinalizadoParaPagamentoState()
        
    def desistir(self, pedido):
        pedido.status = PedidoAbandonadoState()


class FinalizadoParaPagamentoState(StatusPedido):
    def __init__(self):
        self.nome = "Finalizado para pagamento"
    
    def avancar(self, pedido):
        pedido.status = EmPreparacaoState()
    
    def retroceder(self, pedido):
        pedido.status = EmAtendimentoState()
    
    def desistir(self, pedido):
        pedido.status = PedidoAbandonadoState()


class EmPreparacaoState(StatusPedido):
    def __init__(self):
        self.nome = "Em preparação"
    
    def avancar(self, pedido):
        pedido.status = ProntoParaEntregaState()

class ProntoParaEntregaState(StatusPedido):
    def __init__(self):
        self.nome = "Pronto para entrega"
    
    def avancar(self, pedido):
        pedido.status = Finalizado()
    
    def retroceder(self, pedido):
        pedido.status = EmPreparacaoState()


class Finalizado(StatusPedido):
    def __init__(self):
        self.nome = "Finalizado"
        
        
class PedidoAbandonadoState(StatusPedido):
    def __init__(self):
        self.nome = "Pedido abandonado"
    
    def avancar(self, pedido):
        pedido.status = EmAtendimentoState()
        
status_mapping = {
    "Em Atendimento": EmAtendimentoState(),
    "Finalizado para pagamento": FinalizadoParaPagamentoState(),
    "Em preparação": EmPreparacaoState(),
    "Pronto para entrega": ProntoParaEntregaState(),
    "Finalizado": Finalizado(),
    "Pedido abandonado": PedidoAbandonadoState()
}