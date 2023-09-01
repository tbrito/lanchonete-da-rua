from abc import ABC, abstractmethod

from domain.entities.pedido import Pedido


class PedidoRepositoryChannel(ABC):
    @abstractmethod
    def get_by_id(self, pedido_id: int) -> Pedido:
        """Obter pedido pelo id."""
        pass
    
    @abstractmethod
    def obter_todos_os_pedidos(self) -> list[Pedido]:
        """Obter todos os pedidos."""
        pass

    @abstractmethod
    def obter_pedidos_nao_finalizados(self) -> list[Pedido]:
        """Obter todos os pedidos nao finalizados."""
        pass

    @abstractmethod
    def add(self, pedido):
        """Cadastrar novo pedido."""
        pass

    @abstractmethod
    def update(self, pedido_id: int, pedido):
        """Atualizar um pedido."""    
        pass

    @abstractmethod
    def delete(self, pedido_id: int):
        """Excluir um pedido.""" 
        pass   