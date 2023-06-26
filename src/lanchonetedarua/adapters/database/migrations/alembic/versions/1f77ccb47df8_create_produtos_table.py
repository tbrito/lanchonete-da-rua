"""create produtos table

Revision ID: 1f77ccb47df8
Revises: 206a36fa943e
Create Date: 2023-06-15 20:59:52.558460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f77ccb47df8'
down_revision = '206a36fa943e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'produto',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('descricao', sa.String(100), nullable=False),
        sa.Column('categoria_id', sa.Integer),
        sa.Column('created_at', sa.DateTime())
    )


def downgrade() -> None:
    op.drop_table('produto')
