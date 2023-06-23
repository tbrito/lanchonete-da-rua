import inject
from flask_restx import Resource
from flask import jsonify
from dataclasses import asdict

from domain.services.cliente_service import ClienteService
from web.resources.clientes.cliente_input import ClienteInput
from adapters.mappings.cliente_map import Cliente

api = ClienteInput.api
_cliente = ClienteInput.cliente

@api.route('/<int:cliente_id>')
class Clientes(Resource):
    @api.doc('obter um cliente por id')
    def get(self, cliente_id):
         return "cliente por ID"

    @api.doc('atualiza um cliente por id')
    def put(self, cliente_id):
        return jsonify({'mensagem': 'Cliente atualizado com sucesso'})

    @api.doc('excluir um cliente por id')
    def delete(self, cliente_id):
        return jsonify({'mensagem': 'Cliente deletado com sucesso'})

@api.route('/')
class ClientesNoParameters(Resource):  
    
    def get(self):
        cliente_service = ClienteService() 
        clientes = Cliente.query.all()
        return jsonify([asdict(cliente) for cliente in clientes])

    @api.expect(_cliente, validate=True)
    def post(self):
        return jsonify({'mensagem': 'Cliente criado com sucesso'})