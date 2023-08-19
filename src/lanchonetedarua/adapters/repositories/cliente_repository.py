from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.repositories.cliente_repository_channel import ClienteRepositoryChannel
from adapters.mappings.cliente_db import ClienteDB
from adapters.mappings.cliente_mapper import ClienteMapper

class ClienteRepository(ClienteRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, cliente_id):
        cliente_db = self._session.query(ClienteDB).get(cliente_id)
        return ClienteMapper.map_cliente_db_to_entity(cliente_db)

    def get_all(self):
        clientes_db = self._session.query(ClienteDB).all()
        return ClienteMapper.map_clientes_db_to_entities(clientes_db)

    def get_by_cpf(self, cliente_cpf):
        cliente_db = self._session.query(ClienteDB).filter_by(cpf=cliente_cpf).first()
        return ClienteMapper.map_cliente_db_to_entity(cliente_db)

    def add(self, cliente):
        cliente_db = ClienteMapper.map_entity_to_cliente_db(cliente)
        self._session.add(cliente_db)
        self._session.commit()
        return ClienteMapper.map_cliente_db_to_entity(cliente_db)

    def update(self, cliente_id, cliente_data):
        cliente = self._session.query(ClienteDB).get(cliente_id)
        if cliente:
            cliente.nome = cliente_data.nome
            cliente.cpf = cliente_data.cpf
            cliente.telefone = cliente_data.telefone
            self._session.commit()

    def delete(self, cliente_id):
        cliente = self._session.query(ClienteDB).get(cliente_id)
        if cliente:
            self._session.delete(cliente)
            self._session.commit()