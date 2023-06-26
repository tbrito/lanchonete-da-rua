from domain.entities.produto import Produto
from domain.repositories.produto_repository_channel import ProdutoRepositoryChannel

class ProdutoService:

    def __init__(self, produto_repository: ProdutoRepositoryChannel) -> None:
        self.produto_repository  = produto_repository
 
    def obter_produtos(self):
        return self.produto_repository.get_all()
        
    def criar_produto(self, produto_data):
        self.produto_repository.add(produto_data)

    def obter_produto_por_id(self, produto_id):
        return self.produto_repository.get_by_id(produto_id)
    
    def atualizar_produto(self, produto_id, produto_data):
        self.produto_repository.update(produto_id, produto_data)

    def deletar_produto(self, produto_id):
        self.produto_repository.delete(produto_id)