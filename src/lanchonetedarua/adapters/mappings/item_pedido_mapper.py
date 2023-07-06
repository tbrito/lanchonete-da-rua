from domain.value_objects.item_pedido import ItemPedido
from adapters.mappings.item_pedido_db import ItemPedidoBD

class ItemPedidoMapper:

    @staticmethod
    def map_itens_pedido_db_to_entities(itens_pedido_entity):
        return [ItemPedidoMapper.map_item_pedido_db_to_entity(item_pedido_db) for item_pedido_db in itens_pedido_entity]

    @staticmethod
    def map_item_pedido_db_to_entity(item_pedido_db):
        if item_pedido_db is None:
            return None
        return ItemPedido(
            id=item_pedido_db.id,
            produto_id = item_pedido_db.produto_id,
            pedido_id = item_pedido_db.pedido_id,
            quantidade = item_pedido_db.quantidade,
            valor = item_pedido_db.valor
        )
    
    @staticmethod
    def map_entity_to_item_pedido_db(pedido_id, entity):
        if entity is None:
            return None
        return ItemPedidoBD(
            pedido_id = pedido_id,
            produto_id = entity.produto_id,
            quantidade = entity.quantidade,
            valor = entity.valor
        )