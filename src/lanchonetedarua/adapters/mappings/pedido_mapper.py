from domain.entities.pedido import Pedido
from adapters.mappings.pedido_db import PedidoDB

class PedidoMapper:

    @staticmethod
    def map_pedidos_db_to_entities(pedidos_entity):
        return [PedidoMapper.map_pedido_db_to_entity(pedido_db) for pedido_db in pedidos_entity]

    @staticmethod
    def map_pedido_db_to_entity(pedido_db):
        if pedido_db is None:
            return None
        return Pedido(
            id=pedido_db.id,
            cliente_id = pedido_db.cliente_id,
            session_id = pedido_db.session_id,
            observacoes = pedido_db.observacoes,
            status = pedido_db.status,
            created_at=pedido_db.created_at
        )
    
    @staticmethod
    def map_entity_to_pedido_db(entity):
        if entity is None:
            return None
        return PedidoDB(
            cliente_id = entity.cliente_id,
            session_id = entity.session_id,
            observacoes = entity.observacoes,
            status = entity.status
        )