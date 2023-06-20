from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import mapper
from domain.entities.cliente import Cliente

metadata = MetaData()

cliente_table = Table('cliente', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('nome', String(50), nullable=False),
                      Column('cpf', String(11)),
                      Column('telefone', String(50)),
                      Column('created_at', DateTime))

mapper(Cliente, cliente_table)