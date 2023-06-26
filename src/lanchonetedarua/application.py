import os

from flask import Flask, Blueprint
from flask_restx import Api

from flask_sqlalchemy import SQLAlchemy

from adapters.repositories.cliente_repository import ClienteRepository
from adapters.repositories.pedido_repository import PedidoRepository
from adapters.repositories.categoria_repository import CategoriaRepository
from adapters.repositories.produto_repository import ProdutoRepository
from configuration import get_config

from web.resources.clientes.clientes_resource import api as clientes_ns
from web.resources.produtos.produtos_resource import api as produtos_ns
from web.resources.categorias.categorias_resource import api as categorias_ns
from web.resources.pedidos.pedido_resource import api as pedidos_ns

from domain.services.cliente_service import ClienteService
from domain.services.produto_service import ProdutoService
from domain.services.pedido_service import PedidoService
from domain.services.categoria_service import CategoriaService


from container_di import ContainerDI

db = SQLAlchemy()

def configure_inject() -> None:
    cliente_repository = ClienteRepository(os.getenv('DATABASE_URI'))
    cliente_service = ClienteService(cliente_repository)
    ContainerDI.register(ClienteService, cliente_service)
    ContainerDI.register(ClienteRepository, cliente_service)
    
    pedido_repository = PedidoRepository(os.getenv('DATABASE_URI'))
    pedido_service = PedidoService(pedido_repository)
    ContainerDI.register(PedidoService, pedido_service)
    ContainerDI.register(PedidoRepository, pedido_service)
    
    produto_repository = ProdutoRepository(os.getenv('DATABASE_URI'))
    produto_service = ProdutoService(produto_repository)
    ContainerDI.register(ProdutoService, produto_service)
    ContainerDI.register(ProdutoRepository, produto_service)
    
    categoria_repository = CategoriaRepository(os.getenv('DATABASE_URI'))
    categoria_service = CategoriaService(categoria_repository)
    ContainerDI.register(CategoriaService, categoria_service)
    ContainerDI.register(CategoriaRepository, pedido_service)

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
    api.add_namespace(pedidos_ns, path='/pedidos')

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
