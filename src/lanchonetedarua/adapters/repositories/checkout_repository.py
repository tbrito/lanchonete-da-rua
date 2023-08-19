from sqlalchemy import DateTime, create_engine
from sqlalchemy.orm import sessionmaker

from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from adapters.mappings.checkout_mapper import CheckoutMapper

class CheckoutRepository(CheckoutRepositoryChannel):
    def __init__(self, database_uri: str):
        engine = create_engine(database_uri)
        Session = sessionmaker(engine)
        self._session = Session()

    def add(self, checkout):
        checkout_db = CheckoutMapper.map_entity_to_checkout_db(checkout)
        self._session.add(checkout_db)
        self._session.commit()
        return CheckoutMapper.map_checkout_db_to_entity(checkout_db)