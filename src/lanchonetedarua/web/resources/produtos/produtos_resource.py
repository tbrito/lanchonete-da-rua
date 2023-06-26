from flask_restx import Resource
from container_di import ContainerDI
from domain.services.produto_service import ProdutoService
from domain.services.categoria_service import CategoriaService
from web.resources.produtos.produto_input import ProdutoInput
from web.response_handle.response_handler import ResponseHandler

api = ProdutoInput.api
_produto = ProdutoInput.produto

@api.route('/<int:produto_id>')
class Produtos(Resource):
    @api.doc('obter um produto por id')
    def get(self, produto_id):
         produto_service = ContainerDI.get(ProdutoService)
         produto = produto_service.obter_produto_por_id(produto_id)
         
         if produto:
             ResponseHandler.error('Produto não encontrado',404)
         
         return ResponseHandler.success(produto, status_code=200)

    @api.doc('atualiza um produto por id')
    @api.expect(_produto, validate=True)
    def put(self, produto_id):
        produto_service = ContainerDI.get(ProdutoService)
        
        produto = produto_service.obter_produto_por_id(produto_id)
        
        if produto is None:
            return ResponseHandler.error('Produto não existe', 404)
        
        produto_data = api.payload
        produto = ProdutoInput(**produto_data)
        produto_service.atualizar_produto(produto_id, produto)
        
        return ResponseHandler.success(status_code=204)
    
    @api.doc('excluir um produto por id')
    def delete(self, produto_id):
        produto_service = ContainerDI.get(ProdutoService)
        produto = produto_service.obter_produto_por_id(produto_id)
        
        if produto is None:
            return ResponseHandler.error('Produto não existe', 400)
        
        produto_service.deletar_produto(produto_id)
        return ResponseHandler.success(produto, 'produto deletado com sucesso', 201)
    
@api.route('/categoria/<int:categoria_id>')
class ProdutosByCategoria(Resource):
   
    @api.doc('obter produtos por categoria')
    def get(self, categoria_id):
         produto_service = ContainerDI.get(ProdutoService)
         produtos = produto_service.obter_produtos_por_categoria_id(categoria_id)
         
         if produtos is None:
             return ResponseHandler.error('Categoria não cadastrado', 404)
         
         return ResponseHandler.success(produtos)

@api.route('/')
class ProdutosNoParameters(Resource):
    
    def get(self):
        produto_service = ContainerDI.get(ProdutoService)
        produtos = produto_service.obter_produtos()
        
        return ResponseHandler.success(data=produtos, status_code=200)

    @api.expect(_produto, validate=True)
    def post(self):
        produto_service = ContainerDI.get(ProdutoService)
        produto_data = api.payload
        produto = ProdutoInput(**produto_data)
        
        categoria_service = ContainerDI.get(CategoriaService)
        categoria = categoria_service.obter_categoria_por_id(produto.categoria_id) 
        
        if categoria is None:
            ResponseHandler.error('Categoria não cadastrada')

        produto_service.criar_produto(produto)
        return ResponseHandler.success('produto criado com sucesso', status_code=201)