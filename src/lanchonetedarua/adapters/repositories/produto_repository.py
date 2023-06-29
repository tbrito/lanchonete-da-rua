from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

from domain.repositories.produto_repository_channel import ProdutoRepositoryChannel
from domain.entities.produto import Produto
from adapters.mappings.produto_map import ProdutoDB

class ProdutoRepository(ProdutoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, produto_id):
        produto_db = self._session.query(ProdutoDB).get(produto_id)
        
        if produto_db is null:
            return None
        
        return self._map_produto_db_to_entity(produto_db)

    def get_all(self):
        produtos_entity = self._session.query(ProdutoDB).all()
        return self._map_produtos_db_to_entities(produtos_entity)
    
    def get_all_by_categoria_id(self, categoria_id):
        produtos_entity = self._session.query(ProdutoDB).filter_by(categoria_id=categoria_id).all()
        
        if produtos_entity is None:
            return None
        
        return self._map_produtos_db_to_entities(produtos_entity)

    def add(self, produto):
        produto_db = self._map_entity_to_produto_db(produto)
        self._session.add(produto_db)
        self._session.commit()

    def update(self, produto_id, produto_data):
        produto = self._session.query(ProdutoDB).get(produto_id)
        if produto:
            produto.categoria_id = produto_data.categoria_id,
            produto.descricao = produto_data.descricao,
            self._session.commit()
            
    def update_status(self, produto_id, status):
        produto = self._session.query(ProdutoDB).get(produto_id)
        if produto:
            produto.status = status,
            self._session.commit()

    def delete(self, produto_id):
        produto = self._session.query(ProdutoDB).get(produto_id)
        if produto:
            self._session.delete(produto)
            self._session.commit()

    # mover os métodos de conversão abaixo para uma classe de conversão

    def _map_produtos_db_to_entities(self, produtos_entity):
        return [self._map_produto_db_to_entity(produto_db) for produto_db in produtos_entity]

    def _map_produto_db_to_entity(self, produto_db):
        if produto_db is None:
            return None
        return Produto(
            id=produto_db.id,
            nome=produto_db.nome,
            descricao = produto_db.descricao,
            categoria_id = produto_db.categoria_id,
            created_at=produto_db.created_at
        )
    
    def _map_entity_to_produto_db(self, entity):
        if entity is None:
            return None
        return ProdutoDB(
            nome= entity.nome,
            categoria_id = entity.categoria_id,
            descricao = entity.descricao,
        )
