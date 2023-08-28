from datetime import datetime
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from domain.entities.fila_atendimento import FilaAtendimento

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class FilaAtendimentoDTO:
    pedido_id: int
    recebido_em: datetime
    finalizado_em: datetime

    def __init__(self, fila: FilaAtendimento):
        self.pedido_id = fila.pedido_id
        self.recebido_em = fila.recebido_em
        self.finalizado_em = fila.finalizado_em

    @classmethod
    def from_entity_list(cls, filas):
        return [cls(fila) for fila in filas]