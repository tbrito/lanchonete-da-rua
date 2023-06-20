from flask_restx import Resource
from web.controllers.produtos.produto_input import ProdutoInput

api = ProdutoInput.api
_produto = ProdutoInput.produto

@api.route('/')
class Produtos(Resource):
    @api.doc('lista de produtos')
    def get(self):
        return "obter produtos"

    @api.response(201, 'Produto criado com sucesso')
    @api.doc('inserir um novo produto')
    @api.expect(_produto, validate=True)
    def post(self):
        return "obter produtos"