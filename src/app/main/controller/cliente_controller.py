from flask import request
from flask_restful import Resource

from ..util.cliente_dto import ClienteDto
from ..service.cliente_service import save_new_cliente, get_all_clientes, get_a_cliente

api = ClienteDto.api
_cliente = ClienteDto.cliente


@api.route('/')
class ClienteList(Resource):
    @api.doc('list_of_registered_clientes')
    @api.marshal_list_with(_cliente, envelope='data')
    def get(self):
        """List all registered clientes"""
        return get_all_clientes()

    @api.response(201, 'Cliente registrado com sucesso.')
    @api.doc('criar um novo cliente')
    @api.expect(_cliente, validate=True)
    def post(self):
        """Creates a new cliente """
        data = request.json
        return save_new_cliente(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The cliente identifier')
@api.response(404, 'Cliente not found.')
class Cliente(Resource):
    @api.doc('get a cliente')
    @api.marshal_with(_cliente)
    def get(self, public_id):
        """get a cliente given its identifier"""
        cliente = get_a_cliente(public_id)
        if not cliente:
            api.abort(404)
        else:
            return cliente