import inject
from flask import Blueprint, request, jsonify
from dataclasses import asdict

from domain.services.cliente_service import ClienteService

cliente_controller = Blueprint('cliente_controller', __name__)

@cliente_controller.route('/', methods=['GET'])
@inject.autoparams()
def obter_clientes(cliente_service: ClienteService):
    clientes = cliente_service.obter_clientes()
    return jsonify([asdict(cliente) for cliente in clientes])

@cliente_controller.route('/', methods=['POST'])
def criar_clientes():
    return jsonify({'mensagem': 'Cliente criado com sucesso'})

@cliente_controller.route('/<int:cliente_id>', methods=['GET'])
def obter_cliente(cliente_id):
    return "cliente por ID"

@cliente_controller.route('/<int:cliente_id>', methods=['PUT'])
def atualizar_cliente(cliente_id):
    return jsonify({'mensagem': 'Cliente atualizado com sucesso'})

@cliente_controller.route('/<int:cliente_id>', methods=['DELETE'])
def deletar_cliente(cliente_id):
    return jsonify({'mensagem': 'Cliente deletado com sucesso'})