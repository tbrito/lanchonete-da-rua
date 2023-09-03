import datetime

from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime, String
from sqlalchemy.orm import declarative_base

from adapters.mappings.pedido_db import PedidoDB

Base = declarative_base()

class CheckoutDB(Base):
    __tablename__ = 'checkout'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey(PedidoDB.id))
    valor_total = Column(Float, nullable=False)
    data_pagamento = Column(DateTime, default=datetime.datetime.now())
    created_at = Column(DateTime, default=datetime.datetime.now())
    status_pagamento = Column(String)