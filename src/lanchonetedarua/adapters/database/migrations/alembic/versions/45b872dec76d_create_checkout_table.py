"""create checkout table

Revision ID: 45b872dec76d
Revises: 523857c2e8b1
Create Date: 2023-06-27 19:18:23.836466

"""
from alembic import op
import sqlalchemy as sa
import datetime
from enum import Enum

# revision identifiers, used by Alembic.
revision = '45b872dec76d'
down_revision = '523857c2e8b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'checkout',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('pedido_id', sa.Integer, nullable=True),
        sa.Column('valor_total', sa.Float, nullable=True),
        sa.Column('data_pagamento', sa.DateTime, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=datetime.datetime.now())
    )

def downgrade() -> None:
    op.drop_table('checkout')
