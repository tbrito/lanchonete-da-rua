from abc import ABC, abstractmethod

class PedidoRepositoryChannel(ABC):
    @abstractmethod
    def get_by_id(self, pedido_id):
        """Obter pedido pelo id."""
        pass

    @abstractmethod
    def obter_pedidos_nao_finalizados(self):
        """Obter todos os pedido."""
        pass

    @abstractmethod
    def add(self, pedido):
        """Cadastrar novo pedido."""
        pass

    @abstractmethod
    def update(self, pedido_id, pedido):
        """Atualizar um pedido."""    
        pass
    
    # @abstractmethod
    # def update_status(self, pedido_id, status):
    #     """Atualiza status do pedido"""
    #     pass

    @abstractmethod
    def delete(self, pedido_id):
        """Excluir um pedido.""" 
        pass   