from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import sessionmaker

from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from adapters.mappings.checkout_map import CheckoutDB

class CheckoutRepository(CheckoutRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def add(self, categoria):
        checkout_db = self._map_entity_to_checkout_db(categoria)
        self._session.add(checkout_db)
        self._session.commit()


    # mover os métodos de conversão abaixo para uma classe de conversão

    def _map_entity_to_checkout_db(self, entity):
        if entity is None:
            return None
        return CheckoutDB(
            pedido_id=entity.pedido_id,
            valor_total=entity.valor_total,
            data_pagamento=entity.data_pagamento,
            status=entity.status
        )
