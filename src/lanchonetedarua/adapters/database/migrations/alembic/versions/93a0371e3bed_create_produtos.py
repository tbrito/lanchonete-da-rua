"""create produtos

Revision ID: 93a0371e3bed
Revises: 96b1525983a9
Create Date: 2023-06-25 20:29:01.128246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93a0371e3bed'
down_revision = '96b1525983a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'pedidos',
        sa.Column('categoria_id', sa.Integer, sa.ForeignKey("categoria.id"), nullable=False),
    )

def downgrade() -> None:
    pass
