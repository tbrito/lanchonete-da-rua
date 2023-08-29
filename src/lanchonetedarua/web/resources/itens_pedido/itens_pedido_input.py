from flask_restx import Namespace, fields

class ItensPedidoInput():
    api = Namespace('pedido', description='operações relacionadas a pedidos')
    item_pedido = api.model('item-pedido', {
        'pedido_id': fields.Integer(required=True, description='Id do pedido'),
        'produto_id': fields.Integer(required=True, description='Id do produto'),
        'quantidade': fields.Integer(required=True, description='valor do produto'),
        'valor': fields.Float(required=True, description='valor do produto'),
    })
    
    def __init__(self, pedido_id, produto_id, valor, quantidade):
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.valor = valor
        self.quantidade = quantidade