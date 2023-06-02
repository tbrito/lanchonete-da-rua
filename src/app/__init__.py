# app/__init__.py

from flask_restful import Api
from flask import Blueprint

from .main.controller.cliente_controller import api as lanchonete_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Lanchonete da Rua',
          version='1.0',
          description='rest api da lanchonete'
          )

api.add_namespace(lanchonete_ns, path='/lanchonete')