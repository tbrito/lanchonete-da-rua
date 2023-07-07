from flask_marshmallow import Marshmallow
from marshmallow import fields


ma = Marshmallow()

class CPFSchema(ma.Schema):
    valor = fields.String()
class ObterClienteOutput(ma.Schema):
    id = fields.Integer()
    nome = fields.String()
    cpf = fields.Nested(CPFSchema)
    telefone = fields.String()
    created_at = fields.DateTime()

obter_cliente_output = ObterClienteOutput()
obter_clientes_output = ObterClienteOutput(many=True)