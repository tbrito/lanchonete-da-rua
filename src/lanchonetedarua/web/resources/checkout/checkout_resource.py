from flask_restx import Resource
from domain.services.checkout_service import CheckoutService
from web.resources.checkout.checkout_input import CheckoutInput
from web.response_handle.response_handler import ResponseHandler

from container_di import ContainerDI

api = CheckoutInput.api
# _checkout = CheckoutInput.checkout

@api.route('/<string:pedido_id>/checkout')
class Checkout(Resource):
    @api.doc('Checkout de pedidos')
    def post(self, pedido_id):
        checkout_service = ContainerDI.get(CheckoutService)
        checkout = checkout_service.criar_checkout_para_pedido(pedido_id)

        return ResponseHandler.success(checkout, 'checkout realizado com sucesso', 201)