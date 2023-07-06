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