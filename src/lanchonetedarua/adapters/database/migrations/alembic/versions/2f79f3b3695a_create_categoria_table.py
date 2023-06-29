"""create categoria table

Revision ID: 2f79f3b3695a
Revises: c4dd0c92e679
Create Date: 2023-06-27 17:06:38.481426

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '2f79f3b3695a'
down_revision = 'c4dd0c92e679'
branch_labels = None
depends_on = None


def upgrade() -> None:
    categoria_table = op.create_table(
        'categoria',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, default=datetime.datetime.now()),
    )

    op.bulk_insert(
        categoria_table,
        [
            { "id": 1, "nome": "Lanche" },
            { "id": 2, "nome": "Acompanhamento" },
            { "id": 3, "nome": "Bebida" },
            { "id": 4, "nome": "Sobremesa" },
            { "id": 5, "nome": "Combo" },
        ],
    )


def downgrade() -> None:
    op.drop_table('categoria')
