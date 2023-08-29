from abc import ABC, abstractmethod

class CheckoutRepositoryChannel(ABC):
    @abstractmethod
    def add(self, checkout):
        """Cria checkout para pedido."""
        pass