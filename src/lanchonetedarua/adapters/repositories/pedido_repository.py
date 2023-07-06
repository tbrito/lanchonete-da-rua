from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from adapters.mappings.pedido_db import PedidoDB
from adapters.mappings.pedido_mapper import PedidoMapper

class PedidoRepository(PedidoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, pedido_id):     
        pedido_db = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido_db is None:
            return None
        
        return PedidoMapper.map_pedido_db_to_entity(pedido_db)

    def get_all(self):
        pedidos_db = self._session.query(PedidoDB).all()
        return PedidoMapper.map_pedidos_db_to_entities(pedidos_db)
    
    def get_all_by_cliente_id(self, cliente_id):
        pedidos_db = self._session.query(PedidoDB).all()
        return PedidoMapper.map_pedidos_db_to_entities(pedidos_db)

    def add(self, pedido):
        pedido_db = PedidoMapper.map_entity_to_pedido_db(pedido)
        self._session.add(pedido_db)
        self._session.commit()

    def update(self, pedido_id, pedido_data):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        if pedido:
            pedido.cliente_id = pedido_data.cliente_id,
            pedido.session_id = pedido_data.session_id,
            pedido.observacoes = pedido_data.observacoes,
            pedido.status = pedido_data.status
            self._session.commit()
            
    def update_status(self, pedido_id, status):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        if pedido:
            pedido.status = status
            self._session.commit()

    def delete(self, pedido_id):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        if pedido:
            self._session.delete(pedido)
            self._session.commit()
