from domain.repositories.checkout_repository_channel import CheckoutRepositoryChannel
from adapters.database.data_access.session_manager import SessionManager
from adapters.mappings.checkout_mapper import CheckoutMapper
from adapters.mappings.checkout_db import CheckoutDB
from domain.value_objects.status_pagamento import StatusPagamento

class CheckoutRepository(CheckoutRepositoryChannel):
    def __init__(self, session_manager: SessionManager):
        self._session = session_manager.session

    def add(self, checkout):
        checkout_db = CheckoutMapper.map_from_entity(checkout)
        self._session.add(checkout_db)
        self._session.commit()
        return CheckoutMapper.map_to_entity(checkout_db)
    
    def atualizar_status_pagamento(self, pedido_id, status_pagamento: StatusPagamento):
        checkout_db = self._session.query(CheckoutDB).filter_by(pedido_id=pedido_id).first()
        if checkout_db is not None:
            checkout_db.status_pagamento = status_pagamento.name
            self._session.commit()