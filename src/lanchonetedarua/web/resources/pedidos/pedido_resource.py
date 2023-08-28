from flask_restx import Resource
from domain.value_objects.status_pedido import EmAtendimentoState
from web.resources.pedidos.output.pedido_output import pedidos_output, pedido_output
from web.response_handle.response_handler import ResponseHandler

from domain.services.pedido_service import PedidoService
from web.resources.pedidos.pedido_input import PedidoInput

from container_di import ContainerDI

api = PedidoInput.api
_pedido = PedidoInput.pedido

@api.route('/<int:pedido_id>')
@api.doc(params={'pedido_id': 'Id do Pedido'})
class Pedidos(Resource):
    @api.doc('obter um pedido por id')
    @api.response(404, "Pedido não encontrado")
    @api.response(200, "Sucesso")
    def get(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        pedido = pedido_service.obter_pedido_por_id(pedido_id)
         
        if pedido is None:
            return ResponseHandler.error('Pedido não encontrado',404)
         
        return ResponseHandler.success(pedido, status_code=200)
    
    
@api.route('/<int:pedido_id>/encaminhar-para-pagamento')
@api.doc(params={'pedido_id': 'Id do Pedido'})
class PedidoParaPagamento(Resource):
    @api.doc('Fechar pedido para iniciar processo de pagamento')
    @api.response(404, "Pedido não encontrado")
    @api.response(400, "Erro ao encaminhar pedido")
    @api.response(200, "Sucesso")
    def patch(self, pedido_id):
        pedido_service = ContainerDI.get(PedidoService)
        pedido = pedido_service.obter_pedido_por_id(pedido_id)
        
        if pedido is None:
            return ResponseHandler.error('Pedido não encontrado',404)
        
        if not isinstance(pedido.status, EmAtendimentoState):
            return ResponseHandler.error(f'Não é possível enviar pedidos com o status {pedido.status.nome} para pagamento')
             
        pedido.avancar_status()
        pedido_atualizado = pedido_service.atualizar_pedido(pedido_id, pedido)
        
        if pedido_atualizado is None:
            return ResponseHandler.error("Erro ao atualizar o pedido")
         
        pedido_atualizado_output = pedido_output.dump(pedido_atualizado)
        return ResponseHandler.success(data=pedido_atualizado_output, status_code=201)

@api.route('/')
class PedidosNoParameter(Resource):
    @api.doc('Criar um novo pedido')
    @api.expect(_pedido)
    def post(self):
        pedido_service = ContainerDI.get(PedidoService)

        pedido_data = api.payload
        pedido = PedidoInput(**pedido_data)
        pedido_service.criar_pedido(pedido)
        
        pedido_criado = pedido_output.dump(pedido)

        return ResponseHandler.success(message= 'pedido criado sucesso', data = pedido_criado, status_code=201)
    
    @api.doc('Obter lista de pedidos não finalizados')
    def get(self):
        pedido_service = ContainerDI.get(PedidoService)
       
        lista_pedidos = pedido_service.obter_pedidos_nao_finalizados()
        
        lista_pedidos_output = pedidos_output.dump(lista_pedidos)
        
        return ResponseHandler.success(lista_pedidos_output)
    