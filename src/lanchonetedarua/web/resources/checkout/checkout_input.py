from flask_restx import Namespace, fields

class CheckoutInput():
    api = Namespace('pedido', description='operações relacionadas a pedidos')
    
    pagamento = api.model('pagamento', {
        'id': fields.Integer(description='ID do pagamento'),
        'status': fields.String(description='Status do pagamento', enum=["approved", "rejected"]),
        'external_reference': fields.Integer(description='O ID externo (ID do pedido)')
    })