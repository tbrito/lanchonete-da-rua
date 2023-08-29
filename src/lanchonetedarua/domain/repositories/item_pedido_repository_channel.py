from abc import ABC, abstractmethod

class ItemPedidoRepositoryChannel(ABC):
    @abstractmethod
    def get_by_id(self, item_pedido_id):
        """Obter item do pedido pelo id."""
        pass

    @abstractmethod
    def get_by_pedido_id(self, pedido_id):
        """Obter item do pedido pelo pedido_id."""
        pass

    @abstractmethod
    def add(self, pedido_id, item_pedido):
        """Adicionar novo item para o pedido."""
        pass

    @abstractmethod
    def update(self, item_pedido_id, item_pedido):
        """Atualizar um item de pedido."""    
        pass

    @abstractmethod
    def delete(self, item_pedido_id):
        """Excluir um item de pedido.""" 
        pass   