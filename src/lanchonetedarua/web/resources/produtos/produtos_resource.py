from flask_restx import Resource
from domain.services.produto_service import ProdutoService
from web.resources.produtos.produto_input import ProdutoInput
from flask import jsonify
from dataclasses import asdict

api = ProdutoInput.api
_produto = ProdutoInput.produto

@api.route('/<int:produto_id>')
class Produtos(Resource):
  
    @api.doc('obter um produto por id')
    def get(self, produto_id):
        return "produto por ID"

    @api.doc('atualiza um produto por id')
    def put(self, produto_id):
        return jsonify({'mensagem': 'produto atualizado com sucesso'})

    @api.doc('exclui um produto por id')
    def delete(self, produto_id):
        return jsonify({'mensagem': 'produto deletado com sucesso'})
    
    @api.doc('lista de produtos')
    def get(self):
        return "obter produtos"

    @api.response(201, 'Produto criado com sucesso')
    @api.doc('inserir um novo produto')
    @api.expect(_produto, validate=True)
    def post(self):
        return "obter produtos"
    
@api.route('/')
class ProdutosNoParameters(Resource):  
    
    @api.doc('lista de produtos')
    def get(self):
        produto_service = ProdutoService() 
        produtos = produto_service.obter_produtos()
        return jsonify([asdict(produto) for produto in produtos])

    @api.response(201, 'Produto criado com sucesso')
    @api.doc('inserir um novo produto')
    @api.expect(_produto, validate=True)
    def post(self):
        return jsonify({'mensagem': 'Cliente criado com sucesso'})    