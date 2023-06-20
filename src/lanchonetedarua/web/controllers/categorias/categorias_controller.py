from flask_restx import Resource
from web.controllers.categorias.categoria_input import CategoriaInput

api = CategoriaInput.api
_categoria = CategoriaInput.categoria

@api.route('/')
class Categorias(Resource):
    @api.doc('lista de categorias')
    @api.marshal_list_with(_categoria, envelope='data')
    def get(self):
        return "obter categorias"

    @api.response(201, 'Categoria criada com sucesso')
    @api.doc('salva uma categoria')
    @api.expect(_categoria, validate=True)
    def post(self):
        return "obter categorias"