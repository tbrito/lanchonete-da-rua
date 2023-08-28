import datetime
from typing import Type
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship

from domain.value_objects.status_pedido import StatusPedido
from domain.entities.pedido import Pedido
from .cliente_mapper import ClienteDB

Base = declarative_base()

class PedidoDB(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String())
    cliente_id = Column(Integer, ForeignKey(ClienteDB.id))
    cliente = relationship(ClienteDB)
    observacoes = Column(String())
    status = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now())
    
    @staticmethod
    def map_to_entities(pedidos_entity) -> list[Pedido]:
        return [PedidoDB.map_to_entity(pedido_db) for pedido_db in pedidos_entity]

    @staticmethod
    def map_to_entity(pedido_db) -> Pedido:
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
    
    @staticmethod
    def map_from_entity(entity: Pedido) -> Type['PedidoDB']:
        if entity is None:
            return None
        return PedidoDB(
            cliente_id = entity.cliente_id,
            session_id = entity.session_id,
            observacoes = entity.observacoes,
            status = entity.status.nome
        )