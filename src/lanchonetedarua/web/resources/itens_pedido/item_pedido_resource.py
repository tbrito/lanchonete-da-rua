from flask_restx import Resource
from web.resources.itens_pedido.itens_pedido_input import ItensPedidoInput
from web.response_handle.response_handler import ResponseHandler

from domain.services.pedido_service import PedidoService

from container_di import ContainerDI

api = ItensPedidoInput.api
_item_pedido = ItensPedidoInput.item_pedido

@api.route('/<string:pedido_id>/itens')
class PedidosAdicionarItens(Resource):
    @api.doc('Adicionar um item ao pedido')
    @api.expect(_item_pedido)
    def post(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        
        item_pedido_data = api.payload
        item_pedido = ItensPedidoInput(**item_pedido_data)
        pedido_service.adicionar_item_pedido(pedido_id, item_pedido)

        return ResponseHandler.success('item adicionado com sucesso', 201)

@api.route('/<string:pedido_id>/itens/<string:item_pedido_id>')
class PedidosEditarItens(Resource):
    @api.doc('Atualizar um item do pedido')
    @api.expect(_item_pedido, validate=True)
    def put(self, pedido_id, item_pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        item_pedido_data = api.payload
        item_pedido = ItensPedidoInput(**item_pedido_data)
        pedido_service.editar_item_pedido(pedido_id, item_pedido_id, item_pedido)
        return ResponseHandler.success(item_pedido, 'item editado com sucesso', 201)

    @api.doc('excluir um item pedido por id')
    def delete(self, pedido_id, item_pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        item_pedido = pedido_service.obter_item_pedido_por_id(item_pedido_id)
        
        if item_pedido is None:
            return ResponseHandler.error('Pedido não existe', 404)
        
        pedido_service.deletar_item_pedido(item_pedido)
        return ResponseHandler.success(item_pedido, 'item do pedido excluido com sucesso', 201)