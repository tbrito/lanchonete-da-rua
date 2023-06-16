from flask import Blueprint

customer_controller = Blueprint('customer_controller', __name__)

@customer_controller.route('/')
def get():
    return "obter clientes"

@customer_controller.route('/')
def post():
    return "obter clientes"