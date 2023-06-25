from sqlalchemy import Column, Enum, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import JSON

from domain.value_objects.status_pedido import StatusPedido
from .cliente_map import ClienteDB

Base = declarative_base()

class PedidoDB(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey(ClienteDB.id))
    cliente = relationship(ClienteDB)
    itens = Column(JSON)
    observacoes = Column(String())
    status = Column(Enum(StatusPedido))
    created_at = Column(DateTime)
    