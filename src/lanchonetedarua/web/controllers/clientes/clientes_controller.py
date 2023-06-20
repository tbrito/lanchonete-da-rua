import inject
from flask_restx import Resource
from flask import jsonify
from dataclasses import asdict

from domain.services.cliente_service import ClienteService
from web.controllers.clientes.cliente_input import ClienteInput

api = ClienteInput.api
_cliente = ClienteInput.cliente

@api.route('/<int:cliente_id>')
class Clientes(Resource):
    # @api.doc('lista de clientes')
    # @api.marshal_list_with(_categorias, envelope='data')

    @api.doc('obter um cliente por id')
    def get(self, cliente_id):
         return "cliente por ID"

    def put(self, cliente_id):
        return jsonify({'mensagem': 'Cliente atualizado com sucesso'})

    def delete(self, cliente_id):
        return jsonify({'mensagem': 'Cliente deletado com sucesso'})
    
@api.route('/')
class ClientesPost(Resource):  
     @inject.autoparams()
     def get(self, cliente_service: ClienteService):
        clientes = cliente_service.obter_clientes()
        return jsonify([asdict(cliente) for cliente in clientes])

     @api.expect(_cliente, validate=True)
     def post(self):
        return jsonify({'mensagem': 'Cliente criado com sucesso'})