from flask_restx import Resource
from flask import jsonify
from flask import request

from domain.entities.cliente import Cliente
from domain.services.cliente_service import ClienteService
from web.resources.clientes.cliente_input import ClienteInput

from container_di import ContainerDI

api = ClienteInput.api
_cliente = ClienteInput.cliente

@api.route('/<int:cliente_id>')
class Clientes(Resource):
    @api.doc('obter um cliente por id')
    def get(self, cliente_id):
         cliente_service = ContainerDI.get(ClienteService)
         cliente = cliente_service.obter_cliente_por_id(cliente_id)
         return jsonify(cliente)

    @api.doc('atualiza um cliente por id')
    def put(self, cliente_id, cliente):
        cliente_service = ContainerDI.get(ClienteService)
        cliente_service.atualizar_cliente(cliente_id, cliente)
        return jsonify({'mensagem': 'Cliente atualizado com sucesso'})

    @api.doc('excluir um cliente por id')
    def delete(self, cliente_id):
        cliente_service = ContainerDI.get(ClienteService)
        cliente_service.deletar_cliente(cliente_id)
        return jsonify({'mensagem': 'Cliente deletado com sucesso'})

@api.route('/')
class ClientesNoParameters(Resource):
    
    def get(self):
        cliente_service = ContainerDI.get(ClienteService)
        clientes = cliente_service.obter_clientes()
        return jsonify(clientes)

    @api.expect(_cliente, validate=True)
    def post(self):
        cliente_service = ContainerDI.get(ClienteService)
        cliente_json = request.get_json() 
        cliente = Cliente.from_dict(cliente_json)
        cliente_service.criar_cliente(cliente)
        return jsonify({'mensagem': 'Cliente criado com sucesso'})