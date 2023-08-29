from flask_restx import Resource
from container_di import ContainerDI
from domain.services.fila_atendimento_service import FilaAtendimentoService
from web.resources.fila_atendimento.fila_input import FilaAtendimentoInput
from web.resources.fila_atendimento.fila_dto import FilaAtendimentoDTO
from web.response_handle.response_handler import ResponseHandler

api = FilaAtendimentoInput.api

@api.route('/na-fila')
class FilaAtendimentoNoParameters(Resource):
    
    def get(self):
        fila_atendimento_service = ContainerDI.get(FilaAtendimentoService)
        filas = fila_atendimento_service.obter_fila_cozinha()
        filas_dto = FilaAtendimentoDTO.from_entity_list(filas)
        return ResponseHandler.success(filas_dto)