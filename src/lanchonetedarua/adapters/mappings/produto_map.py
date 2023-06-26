from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import JSON

from adapters.mappings.categoria_map import CategoriaDB
from .cliente_map import ClienteDB

Base = declarative_base()

class ProdutoDB(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    categoria_id = Column(Integer, ForeignKey(CategoriaDB.id))
    categoria = relationship(CategoriaDB)
    descricao = Column(String())
    created_at = Column(DateTime())