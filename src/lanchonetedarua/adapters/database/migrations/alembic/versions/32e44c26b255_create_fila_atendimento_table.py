"""create fila_atendimento table

Revision ID: 32e44c26b255
Revises: 45b872dec76d
Create Date: 2023-06-27 19:26:03.294151

"""
import sqlalchemy as sa
import datetime

from alembic import op
from enum import Enum

# revision identifiers, used by Alembic.
revision = '32e44c26b255'
down_revision = '45b872dec76d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'fila_atendimento',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('pedido_id', sa.Integer, nullable=False),
        sa.Column('recebido_em', sa.DateTime, nullable=False, default=datetime.datetime.now()),
        sa.Column('finalizado_em', sa.DateTime, nullable=True)
    )

def downgrade() -> None:
    op.drop_table('fila_atendimento')
