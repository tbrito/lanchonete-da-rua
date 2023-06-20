from abc import ABC, abstractmethod

class ClienteRepositoryChannel(ABC):
    @abstractmethod
    def get_by_id(self, cliente_id):
        """Obter usuario pelo id."""
        pass

    @abstractmethod
    def get_by_cpf(self, cliente_cpf):
        """Cadastrar usuário pelo cpf."""  
        pass  

    @abstractmethod
    def get_all(self):
        """Obter todos os usuário."""
        pass

    @abstractmethod
    def add(self, cliente):
        """Cadastrar novo usuário."""
        pass

    @abstractmethod
    def update(self, cliente_id, cliente):
        """Atualizar um usuário."""    
        pass

    @abstractmethod
    def delete(self, cliente_id):
        """Excluir um usuário.""" 
        pass   