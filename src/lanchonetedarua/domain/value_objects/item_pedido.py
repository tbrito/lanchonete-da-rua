class ItemPedido():
    id: int
    valor: float
    pedido_id: int
    produto_id: int
    quantidade: int
    
    def __init__(self, id, valor, pedido_id, produto_id, quantidade):
        self.id = id
        self.valor = valor
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = quantidade

