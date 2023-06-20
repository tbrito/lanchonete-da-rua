from enum import Enum

class StatusPedido(Enum):
    EM_ATENDIMENTO = "Em atendimento"
    FINALIZADO_PARA_PAGAMENTO = "Pedido finalizado aguardando pagamento"
    AGUARDANDO_PREPARO = "Pedido pago aguardando início do preparo"
    EM_PREPARACAO = "Em preparação"
    PRONTO_PARA_ENTREGA = "Pronto para entrega"
    ENTREGUE = "Entregue"