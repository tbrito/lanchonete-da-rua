from flask_restx import Resource
from domain.services.checkout_service import CheckoutService
from domain.value_objects.status_pagamento import StatusPagamento
from web.resources.checkout.checkout_input import CheckoutInput
from web.resources.checkout.checkout_dto import CheckoutDTO
from web.response_handle.response_handler import ResponseHandler

from container_di import ContainerDI

api = CheckoutInput.api
_pagamento = CheckoutInput.pagamento

@api.route('/<string:pedido_id>/checkout')
class Checkout(Resource):
    @api.doc('Checkout de pedidos')
    def post(self, pedido_id):
        checkout_service = ContainerDI.get(CheckoutService)
        
        checkout = checkout_service.criar_checkout_para_pedido(pedido_id)
        
        if(isinstance(checkout, str)):
            return ResponseHandler.error(checkout, 400)
        
        checkkout_dto = CheckoutDTO(checkout)
        
        return ResponseHandler.success(data=checkkout_dto, status_code=201)
    
@api.route('/pagamento-webhook')
class AtualizaPagamentoPedidoWebhook(Resource):
    @api.doc('Webhook para atualização do status do pagamento do pedido')
    @api.expect(_pagamento)
    def post(self):
        try:
            checkout_service = ContainerDI.get(CheckoutService)
            pedido_id = api.payload['external_reference']
            status_pagamento = StatusPagamento(api.payload['status'])
            checkout_service.atualizar_status_pagamento(pedido_id, status_pagamento)
            return ResponseHandler.success("Dados recebidos com sucesso.", status_code=201)
        except Exception as e:
            return ResponseHandler.error(str(e), status_code=400)
        
@api.route('/<string:pedido_id>/status-pagamento')
class ConsultaStatusPagamentoPedido(Resource):
    @api.doc('Consulta status do pagamento do pedido')
    def get(self, pedido_id):
        checkout_service = ContainerDI.get(CheckoutService)
        status_pagamento = checkout_service.obter_status_pagamento(pedido_id)
        if status_pagamento is None:
            return ResponseHandler.error("Status não encontrado", status_code=404)
        return ResponseHandler.success(status_pagamento)