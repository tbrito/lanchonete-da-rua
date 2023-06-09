from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json, LetterCase

from .entity import Entity

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Checkout(Entity):
    pedido_id: int
    valor_total: float
    data_pagamento: datetime
    def __init__(self, id, pedido_id, valor_total, data_pagamento, created_at):
        super().__init__(id, created_at)
        self.pedido_id = pedido_id
        self.valor_total = valor_total
        self.data_pagamento = data_pagamento