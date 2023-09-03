from abc import ABC, abstractmethod

class CheckoutRepositoryChannel(ABC):
    @abstractmethod
    def add(self, checkout):
        """Cria checkout para pedido."""
        pass

    @abstractmethod
    def atualizar_status_pagamento(self, pedido_id, status_pagamento):
        """Atualiza status do pagamento de um pedido."""
        pass

    @abstractmethod
    def obter_status_pagamento(self, pedido_id):
        """Consulta status do pagamento de um pedido."""
        pass