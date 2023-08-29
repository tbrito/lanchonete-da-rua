from flask_restx import Namespace, fields

class CheckoutInput():
    api = Namespace('pedido', description='operações relacionadas a pedidos')
