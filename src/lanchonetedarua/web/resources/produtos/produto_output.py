from flask_marshmallow import Marshmallow
from marshmallow import fields


ma = Marshmallow()

class CategoriaSchema(ma.Schema):
    valor = fields.String()

class ProdutoOutput(ma.Schema):
    id = fields.Integer()
    nome = fields.String()
    descricao = fields.String()
    categoria = fields.Nested(CategoriaSchema)
    created_at = fields.DateTime()

produto_output = ProdutoOutput()
produtos_output = ProdutoOutput(many=True)