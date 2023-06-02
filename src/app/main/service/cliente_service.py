import uuid
import datetime

from app.main import db
from app.main.model.cliente import Cliente


def save_new_customer(data):
    cliente = Cliente.query.filter_by(telefone=data['telefone']).first()
    if not cliente:
        new_user = Cliente(
            public_id=str(uuid.uuid4()),
            telefone=data['telefone'],
            nome=data['nome'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Registrado com sucesso.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Cliente já existe.',
        }
        return response_object, 409


def get_all_clientes():
    return Cliente.query.all()


def get_a_cliente(public_id):
    return Cliente.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()