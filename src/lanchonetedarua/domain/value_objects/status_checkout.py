from enum import Enum

class StatusCheckout(Enum):
    AGUARDANDO_PAGAMENTO = "Aguardando pagamento"
    PAGO = "Pedido pago"
    ABANDONADO = "Checkout abandonado"