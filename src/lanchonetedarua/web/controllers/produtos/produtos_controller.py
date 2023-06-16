from flask import Blueprint

produtos_controller = Blueprint('produtos_controller', __name__)

@produtos_controller.route('/')
def get():
    return "obter produtos"

@produtos_controller.route('/')
def post():
    return "obter produtos"