"""create categoria table

Revision ID: 8f2a84a9b605
Revises: 1f77ccb47df8
Create Date: 2023-06-15 21:01:17.392874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f2a84a9b605'
down_revision = '1f77ccb47df8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'categoria',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('categoria')
