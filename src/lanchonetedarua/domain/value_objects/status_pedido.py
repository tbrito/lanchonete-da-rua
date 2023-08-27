
class StatusPedido:
    def avancar(self, pedido):
        pass
    
    def retroceder(self, pedido):
        pass
    
    def desistir(self, pedido):
        pass


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
        pedido.status = AguardandoPreparoState()
    
    def retroceder(self, pedido):
        pedido.status = EmAtendimentoState()
    
    def desistir(self, pedido):
        pedido.status = PedidoAbandonadoState()


class AguardandoPreparoState(StatusPedido):
    def __init__(self):
        self.nome = "Aguardando preparo"
        
    def avancar(self, pedido):
        pedido.status = EmPreparacaoState()
    
    def retroceder(self, pedido):
        pedido.status = FinalizadoParaPagamentoState()


class EmPreparacaoState(StatusPedido):
    def __init__(self):
        self.nome = "Em preparação"
    
    def avancar(self, pedido):
        pedido.status = ProntoParaEntregaState()
    
    def retroceder(self, pedido):
        pedido.status = AguardandoPreparoState()


class ProntoParaEntregaState(StatusPedido):
    def __init__(self):
        self.nome = "Pronto para entrega"
    
    def avancar(self, pedido):
        pedido.status = Finalizado()
    
    def retroceder(self, pedido):
        pedido.status = EmPreparacaoState()


class Finalizado(StatusPedido):
    def __init__(self):
        self.nome = "Entregue"
        
        
class PedidoAbandonadoState(StatusPedido):
    def avancar(self, pedido):
        pedido.estato = EmAtendimentoState()