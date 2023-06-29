from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, declarative_base, relationship, mapped_column

from adapters.mappings.produto_map import ProdutoDB
from adapters.mappings.pedido_map import PedidoDB

Base = declarative_base()

class ItemPedidoBD(Base):
    # __allow_unmapped__ = True
    __tablename__ = 'item_pedido'

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey(PedidoDB.id))
    pedido = relationship(PedidoDB)
    produto_id = Column(Integer, ForeignKey(ProdutoDB.id))
    produto = relationship(ProdutoDB)
    
    valor = Column(Float)
    quantidade = Column(Integer)

    
    