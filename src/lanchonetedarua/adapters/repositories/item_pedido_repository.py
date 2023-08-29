from domain.repositories.item_pedido_repository_channel import ItemPedidoRepositoryChannel
from adapters.database.data_access.session_manager import SessionManager
from adapters.mappings.item_pedido_db import ItemPedidoBD
from adapters.mappings.item_pedido_mapper import ItemPedidoMapper

class ItemPedidoRepository(ItemPedidoRepositoryChannel):
    def __init__(self, session_manager: SessionManager):
        self._session = session_manager.session

    def get_by_id(self, item_pedido_id):
        item_pedido_db = self._session.query(ItemPedidoBD).get(item_pedido_id)
        
        if item_pedido_db is None:
            return None
        
        return ItemPedidoMapper.map_item_pedido_db_to_entity(item_pedido_db)

    def get_by_pedido_id(self, pedido_id):
        itens_pedido_db = self._session.query(ItemPedidoBD).filter_by(pedido_id=pedido_id)
        return ItemPedidoMapper.map_itens_pedido_db_to_entities(itens_pedido_db)
  
    def add(self, pedido_id, item_pedido):
        item_pedido_db = ItemPedidoMapper.map_entity_to_item_pedido_db(pedido_id, item_pedido)
        self._session.add(item_pedido_db)
        self._session.commit()
        return ItemPedidoMapper.map_item_pedido_db_to_entity(item_pedido_db)

    def update(self, item_pedido_id, item_pedido):
        item_pedido_db = self._session.query(ItemPedidoBD).get(item_pedido_id)
        if item_pedido_db:
            item_pedido_db.pedido_id = item_pedido.pedido_id,
            item_pedido_db.produto_id = item_pedido.produto_id,
            item_pedido_db.quantidade = item_pedido.quantidade,
            item_pedido_db.valor = item_pedido.valor
            self._session.commit()
  
    def delete(self, item_pedido_id):
        item_pedido_db = self._session.query(ItemPedidoBD).get(item_pedido_id)
        if item_pedido_db:
            self._session.delete(item_pedido_db)
            self._session.commit()
