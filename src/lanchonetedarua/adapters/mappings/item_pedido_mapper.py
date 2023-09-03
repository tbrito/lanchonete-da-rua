from domain.value_objects.item_pedido import ItemPedido
from adapters.mappings.item_pedido_db import ItemPedidoBD

class ItemPedidoMapper:

    @staticmethod
    def map_to_entities(itens_pedido_entity):
        return [ItemPedidoMapper.map_to_entity(item_pedido_db) for item_pedido_db in itens_pedido_entity]

    @staticmethod
    def map_to_entity(item_pedido_db):
        if item_pedido_db is None:
            return None
        item_pedido = ItemPedido(
            id=item_pedido_db.id,
            produto_id = item_pedido_db.produto_id,
            pedido_id = item_pedido_db.pedido_id,
            quantidade = item_pedido_db.quantidade,
            valor = item_pedido_db.valor
        )
        
        item_pedido.produto = item_pedido_db.produto
        
        return item_pedido
    
    @staticmethod
    def map_from_entity(pedido_id, entity):
        if entity is None:
            return None
        return ItemPedidoBD(
            pedido_id = pedido_id,
            produto_id = entity.produto_id,
            quantidade = entity.quantidade,
            valor = entity.valor
        )