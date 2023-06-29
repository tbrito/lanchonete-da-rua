from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import sessionmaker

from adapters.mappings.fila_atendimento_map import FilaAtendimentoDB
from domain.entities.fila_atendimento import FilaAtendimento
from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel

class FilaAtendimentoRepository(FilaAtendimentoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, fila_id):
        fila_db = self._session.query(FilaAtendimentoDB).get(fila_id)
        return self._map_fila_db_to_entity(fila_id)

    def get_all(self):
        filas_entity = self._session.query(FilaAtendimentoDB).all()
        return self._map_fila_db_to_entities(filas_entity)

    def add(self, fila):
        fila_db = self._map_entity_to_fila_db(fila)
        self._session.add(fila_db)
        self._session.commit()

    def delete(self, fila_id):
        fila = self._session.query(FilaAtendimentoDB).get(fila_id)
        if fila:
            self._session.delete(fila)
            self._session.commit()

    # mover os métodos de conversão abaixo para uma classe de conversão

    def _map_fila_db_to_entities(self, fila_entity):
        return [self._map_fila_db_to_entity(fila_db) for fila_db in fila_entity]

    def _map_fila_db_to_entity(self, fila_db):
        if fila_db is None:
            return None
        return FilaAtendimento(
            id=fila_db.id,
            pedido_id=fila_db.pedido_id,
            recebido_em=fila_db.recebido_em,
            finalizado_em=fila_db.finalizado_em
        )
    
    def _map_entity_to_fila_db(self, entity):
        if entity is None:
            return None
        return FilaAtendimentoDB(
            pedido_id=entity.pedido_id,
            recebido_em=entity.recebido_em,
            finalizado_em=entity.finalizado_em
        )
