from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from adapters.database.data_access.session_manager import SessionManager
from adapters.mappings.checkout_mapper import CheckoutMapper

class CheckoutRepository(CheckoutRepositoryChannel):
    def __init__(self, session_manager: SessionManager):
        self._session = session_manager.session

    def add(self, checkout):
        checkout_db = CheckoutMapper.map_entity_to_checkout_db(checkout)
        self._session.add(checkout_db)
        self._session.commit()
        return CheckoutMapper.map_checkout_db_to_entity(checkout_db)