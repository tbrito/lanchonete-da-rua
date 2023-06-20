from domain.entities.produto import Produto

class ProdutoService:

    def obter_produtos(self):
        # Lógica para obter produtos do domínio. Mock:
        produtos = [Produto(1, "XBurguer", "P"),
                    Produto(2, "XBurguer", "G"),
                    Produto(3, "XSalada", "P"),
                    Produto(4, "XSalada", "G"),
                    Produto(5, "XPodrao", "P"),
                    Produto(6, "XPodrao", "G")]
        return produtos

    def criar_produto(self, produto_data):
        # Lógica para persistir o produto no domínio
        ...

    def obter_produto_por_id(self, produto_id):
        # Lógica para obter um produto pelo ID do domínio
        ...

    def atualizar_produto(self, produto_id, produto_data):
        # Lógica para atualizar um produto no domínio
        ...

    def deletar_produto(self, produto_id):
        # Lógica para deletar um produto do domínio
        ...