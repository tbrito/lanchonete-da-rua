from flask_restful import Namespace, fields


class ClienteDto:
    api = Namespace('cliente', description='operacoes relacionadas a clienete')
    cliente = api.model('cliente', {
        'telefone': fields.String(required=True, description='telefone do cliente'),
        'nome': fields.String(required=True, description='nome do cliente')
    })