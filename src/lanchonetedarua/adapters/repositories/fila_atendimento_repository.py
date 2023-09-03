import datetime

from domain.repositories.fila_atendimento_repository_channel import FilaAtendimentoRepositoryChannel
from adapters.database.data_access.session_manager import SessionManager
from adapters.mappings.fila_atendimento_db import FilaAtendimentoDB
from adapters.mappings.fila_atendimento_mapper import FilaAtendimentoMapper

class FilaAtendimentoRepository(FilaAtendimentoRepositoryChannel):
    def __init__(self, session_manager: SessionManager):
        self._session = session_manager.session

    def get_by_id(self, fila_id):
        fila_db = self._session.query(FilaAtendimentoDB).get(fila_id)
        return FilaAtendimentoMapper.map_fila_db_to_entity(fila_db)

    def get_all(self):
        filas_db = self._session.query(FilaAtendimentoDB).all()
        return FilaAtendimentoMapper.map_fila_db_to_entities(filas_db)
    
    def obter_itens_nao_finalizados(self):
        filas_db = self._session.query(FilaAtendimentoDB).filter(FilaAtendimentoDB.finalizado_em == None).all()
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

    def finalizar_by_pedido_id(self, pedido_id):
        fila = self._session.query(FilaAtendimentoDB).filter_by(pedido_id=pedido_id).first()
        if fila:
            fila.finalizado_em= datetime.datetime.now(),
            self._session.commit()