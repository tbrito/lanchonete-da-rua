import secrets
from typing import Type
from flask_restx import Namespace, fields

class PedidoInput():
    cliente_id: int
    session_id: int
    observacoes: str
    api = Namespace('pedido', description='operações relacionadas a pedidos')
    pedido = api.model('pedido', {
        'cliente_id': fields.Integer(required=False, description='Id do cliente'),
        'session_id':  fields.String(required=False, description='Sessão de usuário caso não identificado'),
        'observacoes': fields.String(description='Observações do pedido'),
    })
    
    def __init__(self, cliente_id = None, observacoes = None) -> Type['PedidoInput']:
        self.cliente_id = cliente_id
        self.session_id = None
        if(self.cliente_id is None):
            self.session_id = secrets.token_hex(16)
        self.observacoes = observacoes