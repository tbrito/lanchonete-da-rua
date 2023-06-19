class Item(Entity):
    def __init__(self, id, nome, descricao, preco):
        super().__init__(id)
        self.nome = nome
        self.descricao = descricao
        self.preco = preco