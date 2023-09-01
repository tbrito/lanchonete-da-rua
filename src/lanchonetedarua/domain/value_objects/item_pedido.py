from domain.entities.pedido import Pedido
from domain.entities.produto import Produto


class ItemPedido():
    id: int
    valor: float
    pedido_id: int
    produto_id: int
    quantidade: int
    produto: Produto
    pedido: Pedido    
    def __init__(self, id, valor, pedido_id, produto_id, quantidade):
        self.id = id
        self.valor = valor
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = quantidade

