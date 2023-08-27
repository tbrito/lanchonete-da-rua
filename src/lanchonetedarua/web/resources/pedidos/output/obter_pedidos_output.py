from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()

class StatusPedidoSchema(ma.Schema):
    nome = fields.String()
class ObterPedidosNaoFinalizadosOutput(ma.Schema):
    id = fields.Integer()
    cliente_id = fields.Integer()
    session_id = fields.Integer()
    observacoes = fields.String()
    status = fields.Nested(StatusPedidoSchema)
    created_at = fields.DateTime()


obter_pedido_output = ObterPedidosNaoFinalizadosOutput()
obter_pedidos_output = ObterPedidosNaoFinalizadosOutput(many=True)