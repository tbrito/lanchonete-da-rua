import os

from flask import Flask, Blueprint
from flask_restx import Api

from flask_sqlalchemy import SQLAlchemy

from adapters.repositories.cliente_repository import ClienteRepository
from configuration import get_config

from web.resources.clientes.clientes_resource import api as clientes_ns
from web.resources.produtos.produtos_resource import api as produtos_ns
from web.resources.categorias.categorias_resource import api as categorias_ns

from domain.services.cliente_service import ClienteService
from domain.services.produto_service import ProdutoService
from domain.repositories.cliente_repository_channel import ClienteRepositoryChannel
from adapters.repositories.cliente_repository import ClienteRepository

from container_di import ContainerDI

db = SQLAlchemy()

def configure_inject() -> None:
    cliente_repository = ClienteRepository(os.getenv('DATABASE_URI'))
    cliente_service = ClienteService(cliente_repository)
    ContainerDI.register(ClienteService, cliente_service)
    ContainerDI.register(ClienteRepository, cliente_service)

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
    app.config.from_object(get_config('dev'))
    db.init_app(app)
    
    configure_inject()
    register_routers(app)
    return app

app = create_app()

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')
