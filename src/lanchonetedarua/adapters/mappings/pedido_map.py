import datetime
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, declarative_base, relationship, mapped_column
from typing import List

from domain.value_objects.status_pedido import StatusPedido
from .cliente_map import ClienteDB

Base = declarative_base()

class PedidoDB(Base):
    # __allow_unmapped__ = True
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String())
    cliente_id = Column(Integer, ForeignKey(ClienteDB.id))
    cliente = relationship(ClienteDB)
    observacoes = Column(String())
    status = Column(Enum(StatusPedido))
    created_at = Column(DateTime, default=datetime.datetime.now())