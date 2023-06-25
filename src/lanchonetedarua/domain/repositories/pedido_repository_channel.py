from abc import ABC, abstractmethod

class PedidoRepositoryChannel(ABC):
    @abstractmethod
    def get_by_id(self, pedido_id):
        """Obter usuario pelo id."""
        pass

    @abstractmethod
    def get_all(self):
        """Obter todos os usuário."""
        pass

    @abstractmethod
    def add(self, pedido):
        """Cadastrar novo usuário."""
        pass

    @abstractmethod
    def update(self, pedido_id, pedido):
        """Atualizar um usuário."""    
        pass

    @abstractmethod
    def delete(self, pedido_id):
        """Excluir um usuário.""" 
        pass   