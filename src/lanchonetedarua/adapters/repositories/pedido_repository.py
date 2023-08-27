from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.entities.pedido import Pedido
from adapters.mappings.pedido_map import PedidoDB
from domain.value_objects.status_pedido import Finalizado, StatusPedido

class PedidoRepository(PedidoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, pedido_id):
        
        pedido_db = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido_db is null:
            return None
        
        return self._map_pedido_db_to_entity(pedido_db)

    def obter_pedidos_nao_finalizados(self):
        
        status = Finalizado()
        pedidos_entity = self._session.query(PedidoDB).all()
        
        return self._map_pedidos_db_to_entities(pedidos_entity)
    
    def get_all_by_cliente_id(self, cliente_id):
        pedidos_entity = self._session.query(PedidoDB).filter(PedidoDB.cliente_id != cliente_id).all()
        return self._map_pedidos_db_to_entities(pedidos_entity)

    def add(self, pedido: Pedido):
        pedido_db = self._map_entity_to_pedido_db(pedido)
        self._session.add(pedido_db)
        self._session.commit()

    def update(self, pedido_id, pedido_data):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        if pedido:
            pedido.cliente_id = pedido_data.cliente_id
            pedido.session_id = pedido_data.session_id
            pedido.observacoes = pedido_data.observacoes
            pedido.status = pedido.status.avancar()
            self._session.commit()
            
    def delete(self, pedido_id):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        if pedido:
            self._session.delete(pedido)
            self._session.commit()

    # mover os métodos de conversão abaixo para uma classe de conversão

    def _map_pedidos_db_to_entities(self, pedidos_entity):
        return [self._map_pedido_db_to_entity(pedido_db) for pedido_db in pedidos_entity]

    def _map_pedido_db_to_entity(self, pedido_db):
        if pedido_db is None:
            return None
        return Pedido(
            id=pedido_db.id,
            cliente_id = pedido_db.cliente_id,
            session_id = pedido_db.session_id,
            observacoes = pedido_db.observacoes,
            status = StatusPedido.get_status_from_database(pedido_db.status),
            created_at=pedido_db.created_at
        )
    
    def _map_entity_to_pedido_db(self, entity):
        if entity is None:
            return None
        return PedidoDB(
            cliente_id = entity.cliente_id,
            session_id = entity.session_id,
            observacoes = entity.observacoes,
            status = entity.status.nome
        )
