from flask_restx import Resource
from flask import jsonify
from container_di import ContainerDI
from domain.services.categoria_service import CategoriaService
from web.resources.categorias.categoria_input import CategoriaInput

api = CategoriaInput.api
_categoria = CategoriaInput.categoria

@api.route('/<int:categoria_id>')
class Categorias(Resource):
    @api.doc('obter um categoria por id')
    def get(self, categoria_id):
         categoria_service = ContainerDI.get(CategoriaService)
         categoria = categoria_service.obter_categoria_por_id(categoria_id)
         return jsonify(categoria)

    @api.doc('atualiza um categoria por id')
    @api.expect(_categoria, validate=True)
    def put(self, categoria_id):
        categoria_service = ContainerDI.get(CategoriaService)
        categoria_data = api.payload
        categoria = CategoriaInput(**categoria_data)
        categoria_service.atualizar_categoria(categoria_id, categoria)
        
        return jsonify({'mensagem': 'Categoria atualizado com sucesso'})

    @api.doc('excluir um categoria por id')
    def delete(self, categoria_id):
        categoria_service = ContainerDI.get(CategoriaService)
        categoria_service.deletar_categoria(categoria_id)
        return jsonify({'mensagem': 'Categoria deletado com sucesso'})

@api.route('/')
class CategoriasNoParameters(Resource):
    
    def get(self):
        categoria_service = ContainerDI.get(CategoriaService)
        categorias = categoria_service.obter_categorias()
        
        return jsonify(categorias)

    @api.expect(_categoria, validate=True)
    def post(self):
        categoria_service = ContainerDI.get(CategoriaService)
        categoria_data = api.payload
        categoria = CategoriaInput(**categoria_data)
        
        categoria_service.criar_categoria(categoria)
        return jsonify({'mensagem': 'Categoria criado com sucesso'})