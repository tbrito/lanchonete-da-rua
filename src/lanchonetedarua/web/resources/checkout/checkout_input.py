from flask_restx import Namespace, fields

from domain.value_objects.status_checkout import StatusCheckout

class CheckoutInput():
    api = Namespace('pedido', description='operações relacionadas a pedidos')
    checkout = api.model('checkout', {
        'pedido_id': fields.Integer(required=True, description='Id do pedido'),
        'status': fields.String(enum=[status.name for status in StatusCheckout], description='Status do checkout'),
        'valor_total': fields.Float(required=True, description='valor total da compra'),
        'data_pagamento': fields.DateTime(required=False, description='data do pagamento do pedido')
    })
    
    def __init__(self, pedido_id, status, valor_total, data_pagamento):
        self.pedido_id = pedido_id
        self.status = status
        self.valor_total = valor_total
        self.data_pagamento = data_pagamento