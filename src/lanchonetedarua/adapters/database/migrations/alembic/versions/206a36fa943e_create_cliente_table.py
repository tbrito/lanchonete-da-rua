"""create cliente table

Revision ID: 206a36fa943e
Revises: 
Create Date: 2023-06-15 20:55:47.546569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '206a36fa943e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'cliente',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('cpf', sa.String(11)),
        sa.Column('telefone', sa.String(50)),
        sa.Column('created_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('cliente')
