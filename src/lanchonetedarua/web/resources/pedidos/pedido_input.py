from flask_restx import Namespace, fields

from domain.value_objects.status_pedido import StatusPedido

class PedidoInput():
    api = Namespace('pedidos', description='operações relacionadas a pedidos')
    pedido = api.model('pedidos', {
        'cliente_id': fields.Integer(required=True, description='Id do cliente'),
        'itens': fields.Raw(required=True, description='Itens do pedido'),
        'observacoes': fields.String(description='Observações do pedido'),
        'status': fields.String(enum=[status.value for status in StatusPedido], description='Status do pedido')
    })
    
    def __init__(self, cliente_id, itens, observacoes):
        self.cliente_id = cliente_id
        self.itens = itens
        self.observacoes = observacoes