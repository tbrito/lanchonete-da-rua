from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.mappings.fila_atendimento_db import FilaAtendimentoDB
from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel
from adapters.mappings.fila_atendimento_mapper import FilaAtendimentoMapper

class FilaAtendimentoRepository(FilaAtendimentoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, fila_id):
        fila_db = self._session.query(FilaAtendimentoDB).get(fila_id)
        return FilaAtendimentoMapper.map_fila_db_to_entity(fila_db)

    def get_all(self):
        filas_db = self._session.query(FilaAtendimentoDB).all()
        return FilaAtendimentoMapper.map_fila_db_to_entities(filas_db)

    def add(self, fila):
        fila_db = FilaAtendimentoMapper.map_entity_to_fila_db(fila)
        self._session.add(fila_db)
        self._session.commit()

    def delete(self, fila_id):
        fila = self._session.query(FilaAtendimentoDB).get(fila_id)
        if fila:
            self._session.delete(fila)
            self._session.commit()