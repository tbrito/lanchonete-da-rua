import os

from dotenv import load_dotenv
from flask import Flask, Blueprint
from flask_restx import Api

from adapters.database.data_access.session_manager import SessionManager
from adapters.repositories.cliente_repository import ClienteRepository
from adapters.repositories.pedido_repository import PedidoRepository
from adapters.repositories.categoria_repository import CategoriaRepository
from adapters.repositories.produto_repository import ProdutoRepository
from adapters.repositories.item_pedido_repository import ItemPedidoRepository
from domain.services.checkout_service import CheckoutService
from adapters.repositories.checkout_repository import CheckoutRepository
from adapters.repositories.fila_atendimento_repository import FilaAtendimentoRepository
from domain.services.fila_atendimento_service import FilaAtendimentoService

from web.resources.clientes.clientes_resource import api as clientes_ns
from web.resources.produtos.produtos_resource import api as produtos_ns
from web.resources.categorias.categorias_resource import api as categorias_ns
from web.resources.pedidos.pedido_resource import api as pedidos_ns
from web.resources.itens_pedido.item_pedido_resource import api as item_pedido_ns
from web.resources.checkout.checkout_resource import api as checkout_ns
from web.resources.fila_atendimento.fila_atendimento_resource import api as fila_ns

from domain.services.cliente_service import ClienteService
from domain.services.produto_service import ProdutoService
from domain.services.pedido_service import PedidoService
from domain.services.categoria_service import CategoriaService

from container_di import ContainerDI

def configure_inject() -> None:
    database_uri = os.getenv('DATABASE_URI')
    session_manager = SessionManager(database_uri)

    cliente_repository = ClienteRepository(session_manager)
    cliente_service = ClienteService(cliente_repository)
    ContainerDI.register(ClienteService, cliente_service)
    ContainerDI.register(ClienteRepository, cliente_service)
    
    pedido_repository = PedidoRepository(session_manager)
    item_pedido_repository = ItemPedidoRepository(session_manager)
    pedido_service = PedidoService(pedido_repository, item_pedido_repository)
    ContainerDI.register(PedidoService, pedido_service)
    ContainerDI.register(PedidoRepository, pedido_service)
    ContainerDI.register(ItemPedidoRepository, pedido_service)
    
    fila_repository = FilaAtendimentoRepository(session_manager)
    fila_service = FilaAtendimentoService(fila_repository)
    ContainerDI.register(FilaAtendimentoService, fila_service)
    ContainerDI.register(FilaAtendimentoRepository, fila_service)

    checkout_repository = CheckoutRepository(session_manager)
    checkout_service = CheckoutService(checkout_repository, pedido_repository, fila_repository, item_pedido_repository)
    ContainerDI.register(CheckoutService, checkout_service)
    ContainerDI.register(CheckoutRepository, checkout_service)
    ContainerDI.register(FilaAtendimentoRepository, checkout_service)

    produto_repository = ProdutoRepository(session_manager)
    produto_service = ProdutoService(produto_repository)
    ContainerDI.register(ProdutoService, produto_service)
    ContainerDI.register(ProdutoRepository, produto_service)
    
    categoria_repository = CategoriaRepository(session_manager)
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
    api.add_namespace(item_pedido_ns, path='/pedidos')
    api.add_namespace(checkout_ns, path='/pedidos')
    api.add_namespace(fila_ns, path='/pedidos')

    app.register_blueprint(blueprint)

def create_app():
    load_dotenv()
    app = Flask(__name__)
    configure_inject()
    register_routers(app)
    return app

app = create_app()

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')
