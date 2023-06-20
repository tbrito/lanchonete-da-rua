from domain.entities.produto import Produto

class ProdutoService:

    def obter_produtos():
        # Lógica para obter produtos do domínio. Mock:
        produtos = [Produto(1, "XBurguer", "P"),
                    Produto(2, "XBurguer", "G"),
                    Produto(3, "XSalada", "P"),
                    Produto(4, "XSalada", "G"),
                    Produto(5, "XPodrao", "P"),
                    Produto(6, "XPodrao", "G")]
        return produtos

    def criar_produto(produto_data):
        # Lógica para persistir o produto no domínio
        ...

    def obter_produto_por_id(produto_id):
        # Lógica para obter um produto pelo ID do domínio
        ...

    def atualizar_produto(produto_id, produto_data):
        # Lógica para atualizar um produto no domínio
        ...

    def deletar_produto(produto_id):
        # Lógica para deletar um produto do domínio
        ...