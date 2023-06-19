from flask import Flask

from web.post_blueprint import example_blueprint
from web.controllers.clientes.clientes_controller import cliente_controller
from web.controllers.produtos.produtos_controller import produtos_controller
from web.controllers.categorias.categorias_controller import categorias_controller

app = Flask(__name__)
app.register_blueprint(example_blueprint)
app.register_blueprint(cliente_controller, url_prefix='/clientes')
app.register_blueprint(produtos_controller, url_prefix='/produtos')
app.register_blueprint(categorias_controller, url_prefix='/categorias')

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')
