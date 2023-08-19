from flask_restx import Resource
from web.response_handle.response_handler import ResponseHandler

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
         pedido = pedido_service.obter_pedido_por_id(pedido_id)
         
         if pedido:
             ResponseHandler.error('Pedido não encontrado',404)
         
         return ResponseHandler.success(pedido, status_code=200)

@api.route('/')
class PedidosNoParameter(Resource):
    @api.doc('Criar um novo pedido')
    @api.expect(_pedido)
    def post(self):
        pedido_service = ContainerDI.get(PedidoService)

        pedido_data = api.payload
        pedido = PedidoInput(**pedido_data)
        pedido_service.criar_pedido(pedido)

        return ResponseHandler.success(message= 'pedido criado sucesso', status_code=201)
    