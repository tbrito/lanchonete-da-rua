from abc import ABC, abstractmethod

class FilaAtendimentoRepositoryChannel(ABC):
    @abstractmethod
    def get_by_id(self, fila_id):
        """Obter fila pelo id."""
        pass

    @abstractmethod
    def get_all(self):
        """Obter todos os itens da fila."""
        pass

    @abstractmethod
    def add(self, fila):
        """Cadastrar novo item para fila."""
        pass

    @abstractmethod
    def delete(self, fila_id):
        """Excluir um fila.""" 
        pass

    @abstractmethod
    def obter_itens_nao_finalizados(self):
        """Obter todos os itens da fila não finalizados."""
        pass   

    def finalizar_by_pedido_id(self, pedido_id):
        """Finalizar uma fila por pedido.""" 
        pass