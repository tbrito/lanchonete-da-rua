from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.entities.pedido import Pedido
from adapters.mappings.pedido_map import PedidoDB
from domain.repositories.item_pedido_repository_channel import ItemPedidoRepositoryChannel
from adapters.mappings.item_pedido_map import ItemPedidoBD
from adapters.mappings import item_pedido_map

class ItemPedidoRepository(ItemPedidoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, item_pedido_id):
        item_pedido_db = self._session.query(ItemPedidoBD).get(item_pedido_id)
        
        if item_pedido_db is null:
            return None
        
        return self._map_item_pedido_db_to_entity(item_pedido_db)

    def get_by_pedido_id(self, pedido_id):
        itens_pedido_entity = self._session.query(ItemPedidoBD).filter_by(pedido_id=pedido_id)
        return self._map_itens_pedido_db_to_entities(itens_pedido_entity)
  
    def add(self, pedido_id, item_pedido):
        item_pedido_db = self._map_entity_to_item_pedido_db(item_pedido)
        self._session.add(item_pedido_db)
        self._session.commit()

    def update(self, item_pedido_id, item_pedido):
        _item_pedido_db = self._session.query(ItemPedidoBD).get(item_pedido_id)
        if _item_pedido_db:
            _item_pedido_db.pedido_id = item_pedido.pedido_id,
            _item_pedido_db.produto_id = item_pedido.produto_id,
            _item_pedido_db.quantidade = item_pedido.quantidade,
            _item_pedido_db.valor = item_pedido.valor
            self._session.commit()
  
    def delete(self, item_pedido_id):
        item_pedido_db = self._session.query(ItemPedidoBD).get(item_pedido_id)
        if item_pedido_db:
            self._session.delete(item_pedido_db)
            self._session.commit()

    # TODO: mover os métodos de conversão abaixo para uma classe de conversão
    def _map_itens_pedido_db_to_entities(self, itens_pedido_entity):
        return [self._map_item_pedido_db_to_entity(item_pedido_db) for item_pedido_db in itens_pedido_entity]

    def _map_item_pedido_db_to_entity(self, item_pedido_db):
        if item_pedido_db is None:
            return None
        return item_pedido_map(
            id=item_pedido_db.id,
            produto_id = item_pedido_db.produto_id,
            pedido_id = item_pedido_db.pedido_id,
            quantidade = item_pedido_db.quantidade,
            valor = item_pedido_db.valor
        )
    
    def _map_entity_to_item_pedido_db(self, entity):
        if entity is None:
            return None
        return ItemPedidoBD(
            pedido_id = entity.pedido_id,
            produto_id = entity.produto_id,
            quantidade = entity.quantidade,
            valor = entity.valor
        )
