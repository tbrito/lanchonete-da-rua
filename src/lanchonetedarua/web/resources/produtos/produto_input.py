from flask_restx import Namespace, fields

class ProdutoInput:
    api = Namespace('produtos', description='operações relacionadas a produtos')
    produto = api.model('produtos', {
        'nome': fields.String(required=True, description='nome do produto'),
        'descricao': fields.String(required=True, description='descrição do produto')
    })