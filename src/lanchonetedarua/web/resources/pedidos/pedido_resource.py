import logging
from flask_restx import Resource
from web.resources.pedidos.output.obter_pedidos_output import obter_pedidos_output
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
    
    @api.doc('Obter lista de pedidos não finalizados')
    def get(self):
        pedido_service = ContainerDI.get(PedidoService)
        logging.basicConfig(
            level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.StreamHandler()  # Output logs to console
                # You can add more handlers here (e.g., writing logs to a file)
            ]
        )
        lista_pedidos = pedido_service.obter_pedidos_nao_finalizados()
        
        logging.debug(lista_pedidos)
        lista_pedidos_output = obter_pedidos_output.dump(lista_pedidos)
        logging.debug(lista_pedidos_output)
        return ResponseHandler.success(lista_pedidos_output)
    