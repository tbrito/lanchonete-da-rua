"""create pedidos table

Revision ID: d683894f1364
Revises: 7f7f5ee74d36
Create Date: 2023-06-27 17:06:55.664570

"""
from alembic import op
import sqlalchemy as sa
from enum import Enum
import datetime

class StatusPedido(Enum):
    EM_ATENDIMENTO = "Em atendimento"
    FINALIZADO_PARA_PAGAMENTO = "Pedido finalizado aguardando pagamento"
    AGUARDANDO_PREPARO = "Pedido pago aguardando início do preparo"
    EM_PREPARACAO = "Em preparação"
    PRONTO_PARA_ENTREGA = "Pronto para entrega"
    ENTREGUE = "Entregue"

# revision identifiers, used by Alembic.
revision = 'd683894f1364'
down_revision = '7f7f5ee74d36'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pedido',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey("cliente.id"), nullable=True),
        sa.Column('session_id', sa.String, nullable=False),
        sa.Column('observacoes', sa.String(100)),
        sa.Column('status', sa.Enum(StatusPedido)),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.now()),
    )


def downgrade() -> None:
    op.drop_table('pedido')
