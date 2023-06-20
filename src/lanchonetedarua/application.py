from flask import Flask

import inject
from inject import configure

from mappings import *

from web.post_blueprint import example_blueprint
from web.controllers.clientes.cliente_controller import cliente_controller
from web.controllers.produtos.produtos_controller import produtos_controller
from web.controllers.categorias.categorias_controller import categorias_controller

from domain.services.cliente_service import ClienteService
from domain.services.produto_service import ProdutoService

def configure_inject() -> None:
    def config(binder: inject.Binder) -> None:
        binder.bind(ClienteService, ClienteService)
        binder.bind(ProdutoService, ProdutoService)
    inject.configure(config)

def register_routers(app):
    # register routes
    app.register_blueprint(example_blueprint)
    app.register_blueprint(cliente_controller, url_prefix='/clientes')
    app.register_blueprint(produtos_controller, url_prefix='/produtos')
    app.register_blueprint(categorias_controller, url_prefix='/categorias')
    

def create_app():
    app = Flask(__name__)
    configure_inject()
    register_routers(app)
    return app

app = create_app()

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')
