from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

from domain.repositories.produto_repository_channel import ProdutoRepositoryChannel
from adapters.mappings.produto_mapper import ProdutoMapper
from adapters.mappings.produto_db import ProdutoDB

class ProdutoRepository(ProdutoRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def get_by_id(self, produto_id):
        produto_db = self._session.query(ProdutoDB).get(produto_id)
        
        if produto_db is None:
            return None
        
        return ProdutoMapper.map_produto_db_to_entity(produto_db)

    def get_all(self):
        produtos_db = self._session.query(ProdutoDB).all()
        return ProdutoMapper.map_produtos_db_to_entities(produtos_db)
    
    def get_all_by_categoria_id(self, categoria_id):
        produtos_db = self._session.query(ProdutoDB).filter_by(categoria_id=categoria_id).all()
        
        if produtos_db is None:
            return None
        
        return ProdutoMapper.map_produtos_db_to_entities(produtos_db)

    def add(self, produto):
        produto_db = ProdutoMapper.map_entity_to_produto_db(produto)
        self._session.add(produto_db)
        self._session.commit()
        return ProdutoMapper.map_produto_db_to_entity(produto_db)

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