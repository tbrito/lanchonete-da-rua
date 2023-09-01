from flask_marshmallow import Marshmallow
from marshmallow import fields
from web.resources.produtos.produto_output import ProdutoOutput
from web.resources.pedidos.pedido_output import PedidosOutput


ma = Marshmallow()

class ItemPedidoOutput(ma.Schema):
    id = fields.Integer()
    pedido_id = fields.Integer()
    pedido = fields.Nested(PedidosOutput())
    produto_id = fields.Integer()
    produto = fields.Nested(ProdutoOutput(), many=True)
    valor = fields.Float()
    quantidade = fields.Integer()

pedido_output = ItemPedidoOutput()
pedidos_output = ItemPedidoOutput(many=True)