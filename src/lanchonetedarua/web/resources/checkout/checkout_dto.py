from datetime import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from domain.entities.checkout import Checkout

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class CheckoutDTO:
    pedido_id: int
    valor_total: float
    data_pagamento: datetime

    def __init__(self, checkout: Checkout):
        self.pedido_id = checkout.pedido_id
        self.valor_total = checkout.valor_total
        self.data_pagamento = checkout.data_pagamento

    @classmethod
    def from_entity_list(cls, produtos):
        return [cls(produto) for produto in produtos]