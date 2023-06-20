from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import mapper
from domain.entities.produto import Produto

metadata = MetaData()

produto_table = Table('produto', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('nome', String(50), nullable=False),
                      Column('tamanho', String(5)))

mapper(Produto, produto_table)