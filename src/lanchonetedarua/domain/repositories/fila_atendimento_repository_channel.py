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