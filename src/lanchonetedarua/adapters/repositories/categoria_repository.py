from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import sessionmaker

from domain.repositories.categoria_repository_channel import CategoriaRepositoryChannel
from domain.entities.categoria import Categoria
from adapters.mappings.categoria_map import CategoriaDB

class CategoriaRepository(CategoriaRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, categoria_id):
        categoria_db = self._session.query(CategoriaDB).get(categoria_id)
        return self._map_categoria_db_to_entity(categoria_db)

    def get_all(self):
        categorias_entity = self._session.query(CategoriaDB).all()
        return self._map_categorias_db_to_entities(categorias_entity)

    def add(self, categoria):
        categoria_db = self._map_entity_to_categoria_db(categoria)
        self._session.add(categoria_db)
        self._session.commit()

    def update(self, categoria_id, categoria_data):
        categoria = self._session.query(CategoriaDB).get(categoria_id)
        if categoria:
            categoria.nome = categoria_data.nome
            self._session.commit()

    def delete(self, categoria_id):
        categoria = self._session.query(CategoriaDB).get(categoria_id)
        if categoria:
            self._session.delete(categoria)
            self._session.commit()

    # mover os métodos de conversão abaixo para uma classe de conversão

    def _map_categorias_db_to_entities(self, categorias_entity):
        return [self._map_categoria_db_to_entity(categoria_db) for categoria_db in categorias_entity]

    def _map_categoria_db_to_entity(self, categoria_db):
        if categoria_db is None:
            return None
        return Categoria(
            id=categoria_db.id,
            nome=categoria_db.nome,
            created_at=categoria_db.created_at
        )
    
    def _map_entity_to_categoria_db(self, entity):
        if entity is None:
            return None
        return CategoriaDB(
            nome=entity.nome,
        )
