from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from domain.entities.pedido import Pedido

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PedidoDTO:
    id: int
    cliente_id: int
    observacoes: str
    status: str

    def __init__(self, pedido: Pedido):
        self.id = pedido.id
        self.cliente_id = pedido.cliente_id
        self.observacoes = pedido.observacoes
        self.status = pedido.status

    @classmethod
    def from_entity_list(cls, pedidos):
        return [cls(pedido) for pedido in pedidos]