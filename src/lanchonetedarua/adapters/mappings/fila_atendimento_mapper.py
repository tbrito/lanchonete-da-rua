from domain.entities.fila_atendimento import FilaAtendimento
from adapters.mappings.fila_atendimento_db import FilaAtendimentoDB

class FilaAtendimentoMapper:

    @staticmethod
    def map_fila_db_to_entities(fila_entity):
        return [FilaAtendimentoMapper.map_fila_db_to_entity(fila_db) for fila_db in fila_entity]

    @staticmethod
    def map_fila_db_to_entity(fila_db):
        if fila_db is None:
            return None
        return FilaAtendimento(
            id=fila_db.id,
            pedido_id=fila_db.pedido_id,
            recebido_em=fila_db.recebido_em,
            finalizado_em=fila_db.finalizado_em,
            created_at=fila_db.created_at
        )
    
    @staticmethod
    def map_entity_to_fila_db(entity):
        if entity is None:
            return None
        return FilaAtendimentoDB(
            pedido_id=entity.pedido_id,
            recebido_em=entity.recebido_em,
            finalizado_em=entity.finalizado_em
        )