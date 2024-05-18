"""create column

Revision ID: c405427f98bc
Revises: a8178fe16853
Create Date: 2024-05-17 00:54:18.511015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c405427f98bc'
down_revision: Union[str, None] = 'a8178fe16853'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('password', sa.VARCHAR(), nullable=False))


def downgrade() -> None:
    pass
