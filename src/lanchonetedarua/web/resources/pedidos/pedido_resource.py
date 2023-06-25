from flask_restx import Resource
from web.response_handle.response_handler import ResponseHandler

from domain.services.pedido_service import PedidoService
from domain.services.cliente_service import ClienteService
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

    @api.doc('atualiza um pedido por id')
    @api.expect(_pedido, validate=True)
    def put(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        
        pedido = pedido_service.obter_pedido_por_id(pedido_id)
        
        if pedido is None:
            return ResponseHandler.error('Pedido não existe', 404)
        
        pedido_data = api.payload
        pedido = PedidoInput(**pedido_data)
        pedido_service.atualizar_pedido(pedido_id, pedido)
        
        return ResponseHandler.success(status_code=204)
    
    @api.doc('excluir um pedido por id')
    def delete(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        pedido = pedido_service.obter_pedido_por_id(pedido_id)
        
        if pedido is None:
            return ResponseHandler.error('Pedido não existe', 400)
        
        pedido_service.deletar_pedido(pedido_id)
        return ResponseHandler.success(pedido, 'pedido deletado com sucesso', 201)

@api.route('/')
class PedidosNoParameters(Resource):
    
    def get(self):
        pedido_service = ContainerDI.get(PedidoService)
        pedidos = pedido_service.obter_pedidos()
        
        return ResponseHandler.success(data=pedidos, status_code=200)

    @api.expect(_pedido, validate=True)
    def post(self):
        pedido_service = ContainerDI.get(PedidoService)
        cliente_service = ContainerDI.get(ClienteService)
        pedido_data = api.payload
        pedido = PedidoInput(**pedido_data)

        cliente = cliente_service.obter_cliente_por_id(pedido.cliente_id)
        if cliente is None:
            return ResponseHandler.error("Cliente não cadastrado")
        
        
        pedido_service.criar_pedido(pedido)
        return ResponseHandler.success('pedido criado com sucesso', status_code=201)