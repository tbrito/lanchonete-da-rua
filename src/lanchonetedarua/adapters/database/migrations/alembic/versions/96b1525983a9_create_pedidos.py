"""create pedidos table

Revision ID: 96b1525983a9
Revises: 8f2a84a9b605
Create Date: 2023-06-25 14:02:43.787024

"""
from alembic import op
import sqlalchemy as sa
from enum import Enum

class StatusPedido(Enum):
    EM_ATENDIMENTO = "Em atendimento"
    FINALIZADO_PARA_PAGAMENTO = "Pedido finalizado aguardando pagamento"
    AGUARDANDO_PREPARO = "Pedido pago aguardando início do preparo"
    EM_PREPARACAO = "Em preparação"
    PRONTO_PARA_ENTREGA = "Pronto para entrega"
    ENTREGUE = "Entregue"

# revision identifiers, used by Alembic.
revision = '96b1525983a9'
down_revision = '8f2a84a9b605'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pedido',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('cliente_id', sa.Integer, sa.ForeignKey("cliente.id"), nullable=False),
        sa.Column('itens', sa.JSON(11)),
        sa.Column('observacoes', sa.String(100)),
        sa.Column('status', sa.Enum(StatusPedido)),
        sa.Column('created_at', sa.DateTime),
    )

def downgrade() -> None:
    op.drop_table('pedido')
