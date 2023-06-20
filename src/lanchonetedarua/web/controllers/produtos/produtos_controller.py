import inject
from flask import Blueprint, request, jsonify
from dataclasses import asdict

from domain.services.produto_service import ProdutoService

produtos_controller = Blueprint('produtos_controller', __name__)

@produtos_controller.route('/', methods=['GET'])
@inject.autoparams()
def obter_produtos(produto_service: ProdutoService):
    produtos = produto_service.obter_produtos()
    return jsonify(produtos)

@produtos_controller.route('/', methods=['POST'])
def criar_produtos():
    return jsonify({'mensagem': 'produto criado com sucesso'})

@produtos_controller.route('/<int:produto_id>', methods=['GET'])
def obter_produto(produto_id):
    return "produto por ID"

@produtos_controller.route('/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    return jsonify({'mensagem': 'produto atualizado com sucesso'})

@produtos_controller.route('/<int:produto_id>', methods=['DELETE'])
def deletar_produto(produto_id):
    return jsonify({'mensagem': 'produto deletado com sucesso'})