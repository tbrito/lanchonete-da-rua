from domain.entities.checkout import Checkout
from adapters.mappings.checkout_db import CheckoutDB

class CheckoutMapper:

    @staticmethod
    def map_from_entity(entity: Checkout) -> CheckoutDB:
        if entity is None:
            return None
        return CheckoutDB(
            pedido_id=entity.pedido_id,
            valor_total=entity.valor_total,
            data_pagamento = entity.data_pagamento,
            status_pagamento = entity.status_pagamento
        )
    
    @staticmethod
    def map_to_entity(checkout_db: CheckoutDB) -> Checkout:
        if checkout_db is None:
            return None
        checkout = Checkout(
            id=checkout_db.id,
            pedido_id=checkout_db.pedido_id,
            valor_total=checkout_db.valor_total,
            created_at=checkout_db.created_at
        )
        checkout.data_pagamento = checkout_db.data_pagamento
        checkout.status_pagamento = checkout_db.status_pagamento
        return checkout