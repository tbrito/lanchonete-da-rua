from flask_marshmallow import Marshmallow
from marshmallow import fields


ma = Marshmallow()

class ItemPedidoOutput(ma.Schema):
    id = fields.Integer()
    pedido_id = fields.Integer()
    produto_id = fields.Integer()
    valor = fields.Float()
    quantidade = fields.Integer()

pedido_output = ItemPedidoOutput()
pedidos_output = ItemPedidoOutput(many=True)