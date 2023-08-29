from flask_restx import Resource
from domain.services.cliente_service import ClienteService
from web.response_handle.response_handler import ResponseHandler
from web.resources.clientes.cliente_input import ClienteInput
from web.resources.clientes.cliente_dto import ClienteDTO

from container_di import ContainerDI

api = ClienteInput.api
_cliente = ClienteInput.cliente

@api.route('/<int:cliente_id>')
class Clientes(Resource):
    @api.doc('obter um cliente por id')
    def get(self, cliente_id):
         cliente_service = ContainerDI.get(ClienteService)
         cliente = cliente_service.obter_cliente_por_id(cliente_id)
         cliente_dto = ClienteDTO(cliente)
         #caso o cliente não exista, retorna um erro
         if cliente is None:
            return ResponseHandler.error('Cliente não existe', 404)

         return ResponseHandler.success(cliente_dto)

     
    @api.doc('atualiza um cliente por id')
    @api.expect(_cliente, validate=True)
    def put(self, cliente_id):
        cliente_service = ContainerDI.get(ClienteService)
        
        dados_cliente = cliente_service.obter_cliente_por_id(cliente_id)
        
        if dados_cliente is None:
            return ResponseHandler.error('Cliente não existe')
        
        cliente_data = api.payload
        cliente = ClienteInput(**cliente_data)
        cliente_service.atualizar_cliente(cliente_id, cliente)
        
        return ResponseHandler.success(message='Cliente atualizado com sucesso', status_code=204)

    @api.doc('excluir um cliente por id')
    def delete(self, cliente_id):
        cliente_service = ContainerDI.get(ClienteService)
        
        cliente = cliente_service.obter_cliente_por_id(cliente_id)
        
        if cliente is None:
            return ResponseHandler.error('Cliente não existe', 404)
        
        cliente_service.deletar_cliente(cliente_id)
        return ResponseHandler.success(message='Cliente deletado com sucesso')
    
    
@api.route('/cpf/<string:cpf>')
class ClienteByCPF(Resource):
   
    @api.doc('obter um cliente por cpf')
    def get(self, cpf):
         cliente_service = ContainerDI.get(ClienteService)
         cliente = cliente_service.obter_cliente_por_cpf(cpf)
         if cliente is None:
             return ResponseHandler.error('Cliente não cadastrado', 404)
         
         cliente_dto = ClienteDTO(cliente)
         return ResponseHandler.success(cliente_dto)


@api.route('/')
class ClientesNoParameters(Resource):
    
    @api.doc('Obter todos os clientes')
    def get(self):
        cliente_service = ContainerDI.get(ClienteService)
        clientes = cliente_service.obter_clientes()
        clientes_dto = ClienteDTO.from_entity_list(clientes)
        return ResponseHandler.success(clientes_dto)
    
    @api.doc('Criar um cliente')
    @api.expect(_cliente, validate=True)
    def post(self):
        cliente_service = ContainerDI.get(ClienteService)
        cliente_input = ClienteInput(**api.payload)
        cliente = cliente_service.criar_cliente(cliente_input)
        cliente_dto = ClienteDTO(cliente)
        return ResponseHandler.success(data=cliente_dto, status_code=201)
