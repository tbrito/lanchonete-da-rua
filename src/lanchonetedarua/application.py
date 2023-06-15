from flask import Flask

# from lanchonetedarua.configuration import configure_inject, configure_application
# from lanchonetedarua.web.post_blueprint import create_post_blueprint


# def create_application() -> Flask:
#     application = Flask(__name__)
#     configure_application(application)
#     configure_inject(application)

#     application.register_blueprint(create_post_blueprint(), url_prefix='/api')

#     return application

##########################################################################################
# Instruções temporárias apenas para subir a aplicação e db minimamente funcional

# Criação da instância da aplicação
app = Flask(__name__)

# Rota padrão
@app.route('/')
def index():
    return 'Hello World!'

# Rota com parâmetro
@app.route('/user/<name>')
def user(name):
    return f'Olá, {name}!'

# Execução do servidor localmente
if __name__ == '__main__':
    app.run(host='0.0.0.0')
##########################################################################################