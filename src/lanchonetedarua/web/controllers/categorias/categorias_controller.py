from flask import Blueprint

categorias_controller = Blueprint('categorias_controller', __name__)

@categorias_controller.route('/')
def get():
    return "obter categorias"

@categorias_controller.route('/')
def post():
    return "obter categorias"