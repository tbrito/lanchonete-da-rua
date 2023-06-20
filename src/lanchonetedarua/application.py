from flask import Flask, Blueprint
from flask_restx import Api

import inject
from inject import configure

from mappings import *

from web.controllers.clientes.clientes_controller import api as clientes_ns
from web.controllers.produtos.produtos_controller import api as produtos_ns
from web.controllers.categorias.categorias_controller import api as categorias_ns

from domain.services.cliente_service import ClienteService

def configure_inject() -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(ClienteService, ClienteService)
    inject.configure(config)

def register_routers(app):
    # register routes
    blueprint = Blueprint('api', __name__)

    api = Api(blueprint,
          title='Lanchonete da rua',
          version='1.0',
          description='Api Restful da lanchonete da rua')

    api.add_namespace(categorias_ns, path='/categorias')
    api.add_namespace(clientes_ns, path='/clientes')
    api.add_namespace(produtos_ns, path='/produtos')

    app.register_blueprint(blueprint)

def create_app():
    app = Flask(__name__)

    configure_inject()
    register_routers(app)
    return app

app = create_app()

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')
