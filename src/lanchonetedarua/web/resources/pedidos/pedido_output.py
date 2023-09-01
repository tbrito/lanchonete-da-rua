from flask_marshmallow import Marshmallow
from marshmallow import fields


ma = Marshmallow()

class StatusPedidoSchema(ma.Schema):
    nome = fields.String()
    
class PedidosOutput(ma.Schema):
    id = fields.Integer()
    cliente_id = fields.Integer()
    session_id = fields.String()
    observacoes = fields.String()
    status = fields.Nested(StatusPedidoSchema)
    created_at = fields.DateTime()

pedido_output = PedidosOutput()
pedidos_output = PedidosOutput(many=True)