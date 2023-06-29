"""create cliente table

Revision ID: c4dd0c92e679
Revises: 
Create Date: 2023-06-27 17:06:25.967836

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = 'c4dd0c92e679'
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
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.now())
    )


def downgrade() -> None:
    op.drop_table('cliente')
