from domain.repositories.categoria_repository_channel import CategoriaRepositoryChannel
from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel

class FilaAtendimentoService:

    def __init__(self, fila_atendimento_repository: FilaAtendimentoRepositoryChannel) -> None:
        self.fila_atendimento_repository  = fila_atendimento_repository
 
    def obter_fila_cozinha(self):
        return self.fila_atendimento_repository.obter_itens_nao_finalizados()