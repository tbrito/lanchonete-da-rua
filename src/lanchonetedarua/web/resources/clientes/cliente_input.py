from flask_restx import Namespace, fields

class ClienteInput():
    api = Namespace('clientes', description='operações relacionadas a clientes')
    cliente = api.model('clientes', {
        'nome': fields.String(required=True, description='nome do cliente'),
        'cpf': fields.String(required=True, description='cpf do cliente'),
        'telefone': fields.String(required=True, description='telefone do cliente')
    })
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone