from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.entities.pedido import Pedido
from adapters.mappings.pedido_map import PedidoDB
from domain.value_objects.status_pedido import Finalizado

class PedidoRepository(PedidoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, pedido_id) -> Pedido:
        
        pedido_db = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido_db is None:
            return None
        
        return PedidoDB.map_to_entity(pedido_db)

    def obter_pedidos_nao_finalizados(self):
        status = Finalizado()
        pedidos_entity = self._session.query(PedidoDB).filter(PedidoDB.status != status.nome).all()
        return PedidoDB.map_to_entities(pedidos_entity)
    
    def get_all_by_cliente_id(self, cliente_id):
        pedidos_entity = self._session.query(PedidoDB).filter(PedidoDB.cliente_id == cliente_id).all()
        return PedidoDB.map_to_entities(pedidos_entity)

    def add(self, pedido: Pedido):
        pedido_db = PedidoDB.map_from_entity(pedido)
        self._session.add(pedido_db)
        self._session.commit()

    def update(self, pedido_id: int, pedido: Pedido):
        pedido_db = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido is not None:
            pedido_db.cliente_id = pedido.cliente_id
            pedido_db.session_id = pedido.session_id
            pedido_db.observacoes = pedido.observacoes
            pedido_db.status = pedido.status.nome
            self._session.commit()
            return PedidoDB.map_to_entity(pedido_db)
        
        return None
            
            
    def delete(self, pedido_id):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido is not None:
            self._session.delete(pedido)
            self._session.commit()
            return PedidoDB.map_to_entity(pedido)
        
        return None