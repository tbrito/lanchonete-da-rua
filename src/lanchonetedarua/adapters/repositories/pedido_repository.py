from sqlalchemy import case
from domain.repositories.pedido_repository_channel import PedidoRepositoryChannel
from domain.entities.pedido import Pedido
from adapters.mappings.pedido_mapper import PedidoMapper
from adapters.mappings.pedido_db import PedidoDB
from domain.value_objects.status_pedido import FinalizadoState, PedidoAbandonadoState, status_mapping
from adapters.database.data_access.session_manager import SessionManager
from adapters.mappings.item_pedido_db import ItemPedidoBD
from adapters.mappings.produto_db import ProdutoDB

status_ordering = case(
            (PedidoDB.status == "Em Atendimento", 0),
            (PedidoDB.status == "Finalizado para pagamento", 1),
            (PedidoDB.status == "Em preparação", 2),
            (PedidoDB.status == "Finalizado", 3),
            (PedidoDB.status == "Pedido abandonado", 4)
            ,
            else_ = 5
            )

class PedidoRepository(PedidoRepositoryChannel):
    def __init__(self, session_manager: SessionManager):
        self._session = session_manager.session

    def get_by_id(self, pedido_id) -> Pedido:
        pedido_db = (self._session
                     .query(PedidoDB)
                     .get(pedido_id))

        if pedido_db is None:
            return None
        
        return PedidoMapper.map_to_entity(pedido_db)

    def obter_todos_os_pedidos(self):
        pedidos_entity = (self._session
                    .query(PedidoDB)
                    .order_by(status_ordering.asc(), PedidoDB.created_at.asc())
                    .all())
        
        return PedidoMapper.map_to_entities(pedidos_entity)

    def obter_pedidos_nao_finalizados(self):
        status_finalizado = FinalizadoState()
        status_abandonado = PedidoAbandonadoState()
        

        
        pedidos_entity = (self._session
                          .query(PedidoDB)
                          .filter(PedidoDB.status != (status_finalizado.nome or status_abandonado.nome))
                          .order_by(status_ordering.asc(), PedidoDB.created_at.asc())
                          .all())
        
        return PedidoMapper.map_to_entities(pedidos_entity)
    
    def get_all_by_cliente_id(self, cliente_id):
        pedidos_entity = self._session.query(PedidoDB).filter(PedidoDB.cliente_id == cliente_id).all()
        return PedidoMapper.map_to_entities(pedidos_entity)

    def add(self, pedido: Pedido):
        pedido_db = PedidoDB.map_from_entity(pedido)
        self._session.add(pedido_db)
        self._session.commit()
        return PedidoMapper.map_to_entity(pedido_db)

    def update(self, pedido_id: int, pedido: Pedido):
        pedido_db = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido is not None:
            pedido_db.cliente_id = pedido.cliente_id
            pedido_db.session_id = pedido.session_id
            pedido_db.observacoes = pedido.observacoes
            pedido_db.status = pedido.status.nome
            self._session.commit()
            return PedidoMapper.map_to_entity(pedido_db)
        
        return None
            
            
    def delete(self, pedido_id):
        pedido = self._session.query(PedidoDB).get(pedido_id)
        
        if pedido is not None:
            self._session.delete(pedido)
            self._session.commit()
            return PedidoMapper.map_to_entity(pedido)
        
        return None
