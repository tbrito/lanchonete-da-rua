"""create itens_pedido table

Revision ID: 523857c2e8b1
Revises: d683894f1364
Create Date: 2023-06-27 17:07:02.202349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '523857c2e8b1'
down_revision = 'd683894f1364'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'item_pedido',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('produto_id', sa.Integer, sa.ForeignKey("produto.id"), nullable=False),
        sa.Column('pedido_id', sa.Integer, sa.ForeignKey("pedido.id"), nullable=False),
        sa.Column('quantidade', sa.Integer),
        sa.Column('valor', sa.Float),
    )


def downgrade() -> None:
    op.drop_table('item_pedido')
