from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from domain.repositories.cliente_repository_channel import ClienteRepositoryChannel
from domain.entities.cliente import Cliente
from adapters.mappings.cliente_map import ClienteDB

class ClienteRepository(ClienteRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, cliente_id):
        cliente_db = self._session.query(ClienteDB).get(cliente_id)
        return self._map_cliente_db_to_entity(cliente_db)

    def get_all(self):
        clientes_entity = self._session.query(ClienteDB).all()
        return self._map_clientes_db_to_entities(clientes_entity)

    def get_by_cpf(self, cliente_cpf):
        cliente_db = self._session.query(ClienteDB).filter_by(cpf=cliente_cpf).first()
        return self._map_cliente_db_to_entity(cliente_db)

    def add(self, cliente):
        cliente_db = self._map_entity_to_cliente_db(cliente)
        self._session.add(cliente_db)
        self._session.commit()

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

    # mover os métodos de conversão abaixo para uma classe de conversão

    def _map_clientes_db_to_entities(self, clientes_entity):
        return [self._map_cliente_db_to_entity(cliente_db) for cliente_db in clientes_entity]

    def _map_cliente_db_to_entity(self, cliente_db):
        if cliente_db is None:
            return None
        return Cliente(
            id=cliente_db.id,
            nome=cliente_db.nome,
            cpf=cliente_db.cpf,
            telefone=cliente_db.telefone
        )
    
    def _map_entity_to_cliente_db(self, entity):
        if entity is None:
            return None
        return ClienteDB(
            nome=entity.nome,
            cpf=entity.cpf,
            telefone=entity.telefone
        )
