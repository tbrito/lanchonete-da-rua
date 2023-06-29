import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FilaAtendimentoDB(Base):
    __tablename__ = 'fila_atendimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(String(50), nullable=False)
    recebido_em = Column(DateTime, default=datetime.datetime.now())
    finalizado_em = Column(DateTime)
    
