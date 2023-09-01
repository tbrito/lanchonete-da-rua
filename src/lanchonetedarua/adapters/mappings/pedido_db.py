import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, case
from sqlalchemy.orm import declarative_base, relationship

from adapters.mappings.cliente_db import ClienteDB

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
    
    
    

    
    
    
    