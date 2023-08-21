from flask_restx import Namespace, fields

class PedidoInput():
    cliente_id: int
    session_id: int
    observacoes: str
    api = Namespace('pedido', description='operações relacionadas a pedidos')
    pedido = api.model('pedido', {
        'cliente_id': fields.Integer(required=False, description='Id do cliente'),
        'session_id':  fields.String(required=True, description='Sessao de usuario caso nao identificado'),
        'observacoes': fields.String(description='Observações do pedido'),
    })
    
    def __init__(self, cliente_id, session_id, observacoes):
        self.cliente_id = cliente_id
        self.session_id = session_id
        self.observacoes = observacoes