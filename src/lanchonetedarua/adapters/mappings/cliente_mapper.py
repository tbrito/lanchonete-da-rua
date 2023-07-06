from domain.entities.cliente import Cliente
from adapters.mappings.cliente_db import ClienteDB

class ClienteMapper:

    @staticmethod
    def map_clientes_db_to_entities(clientes_entity):
        return [ClienteMapper.map_cliente_db_to_entity(cliente_db) for cliente_db in clientes_entity]

    @staticmethod
    def map_cliente_db_to_entity(cliente_db):
        if cliente_db is None:
            return None

        return Cliente(
            id=cliente_db.id,
            nome=cliente_db.nome,
            cpf=cliente_db.cpf,
            telefone=cliente_db.telefone,
            created_at=cliente_db.created_at
        )

    @staticmethod
    def map_entity_to_cliente_db(entity):
        if entity is None:
            return None

        return ClienteDB(
            nome=entity.nome,
            cpf=entity.cpf.valor,
            telefone=entity.telefone
        )