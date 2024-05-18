"""add column

Revision ID: d2131323d976
Revises: 3501ba064324
Create Date: 2024-05-17 00:32:28.565471

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2131323d976'
down_revision: Union[str, None] = '3501ba064324'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('password', sa.VARCHAR(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'password')
