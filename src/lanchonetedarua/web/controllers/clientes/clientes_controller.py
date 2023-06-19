from flask import Blueprint, jsonify, request

cliente_controller = Blueprint('cliente_controller', __name__)

@cliente_controller.route('/', methods=['POST'])
def criar_cliente():
    dados_cliente = request.json

    cliente = {
        'nome': dados_cliente['nome'],
        'email': dados_cliente['email'],
    }

    return jsonify(cliente), 201

@cliente_controller.route('/', methods=['GET'])
def obter_clientes():
    clientes = [
        {'nome': 'Cliente 1', 'email': 'cliente1@example.com'},
        {'nome': 'Cliente 2', 'email': 'cliente2@example.com'},
    ]

    return jsonify(clientes)