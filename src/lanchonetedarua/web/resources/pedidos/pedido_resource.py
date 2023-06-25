from flask_restx import Resource
from flask import jsonify

from domain.services.pedido_service import PedidoService
from web.resources.pedidos.pedido_input import PedidoInput

from container_di import ContainerDI

api = PedidoInput.api
_pedido = PedidoInput.pedido

@api.route('/<int:pedido_id>')
class Pedidos(Resource):
    @api.doc('obter um pedido por id')
    def get(self, pedido_id):
         pedido_service = ContainerDI.get(PedidoService)
         pedido = pedido_service.obter_pedidos(pedido_id)
         return jsonify(pedido)

    @api.doc('atualiza um pedido por id')
    @api.expect(_pedido, validate=True)
    def put(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        pedido_data = api.payload
        pedido = PedidoInput(**pedido_data)
        pedido_service.atualizar_pedido(pedido_id, pedido)
        
        return jsonify({'mensagem': 'pedido atualizado com sucesso'})

    @api.doc('excluir um pedido por id')
    def delete(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        pedido_service.deletar_pedido(pedido_id)
        return jsonify({'mensagem': 'pedido deletado com sucesso'})

@api.route('/')
class PedidosNoParameters(Resource):
    
    def get(self):
        pedido_service = ContainerDI.get(PedidoService)
        pedidos = pedido_service.obter_pedidos()
        
        return jsonify(pedidos)

    @api.expect(_pedido, validate=True)
    def post(self):
        pedido_service = ContainerDI.get(PedidoService)
        pedido_data = api.payload
        pedido = PedidoInput(**pedido_data)
        
        pedido_service.criar_pedido(pedido)
        return jsonify({'mensagem': 'pedido criado com sucesso'})