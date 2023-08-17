from domain.entities.checkout import Checkout
from adapters.mappings.checkout_db import CheckoutDB

class CheckoutMapper:

    @staticmethod
    def map_entity_to_checkout_db(entity):
        if entity is None:
            return None
        return CheckoutDB(
            pedido_id=entity.pedido_id,
            valor_total=entity.valor_total,
            data_pagamento=entity.data_pagamento
        )
    
    @staticmethod
    def map_checkout_db_to_entity(checkout_db):
        if checkout_db is None:
            return None
        return Checkout(
            id=checkout_db.id,
            pedido_id=checkout_db.pedido_id,
            valor_total=checkout_db.valor_total,
            data_pagamento=checkout_db.data_pagamento,
            created_at=checkout_db.created_at
        )