from flask_restx import Namespace, fields

from domain.value_objects.status_pedido import StatusPedido

class PedidoInput():
    api = Namespace('pedido', description='operações relacionadas a pedidos')
    pedido = api.model('pedido', {
        'cliente_id': fields.Integer(required=False, description='Id do cliente'),
        'session_id':  fields.String(required=True, description='Sessao de usuario caso nao identificado'),
        'observacoes': fields.String(description='Observações do pedido'),
        'status': fields.String(enum=[status.name for status in StatusPedido], description='Status do pedido'),
    })
    
    def __init__(self, cliente_id, session_id, observacoes, status):
        self.cliente_id = cliente_id
        self.session_id = session_id
        self.observacoes = observacoes
        self.status = status