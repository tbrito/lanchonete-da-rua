from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship

from adapters.mappings.produto_db import ProdutoDB
from adapters.mappings.pedido_db import PedidoDB

Base = declarative_base()

class ItemPedidoBD(Base):
    __tablename__ = 'item_pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey(PedidoDB.id))
    pedido = relationship(PedidoDB)
    produto_id = Column(Integer, ForeignKey(ProdutoDB.id))
    produto = relationship(ProdutoDB)
    
    valor = Column(Float)
    quantidade = Column(Integer)
    

    

    
    