"""drop colume

Revision ID: a8178fe16853
Revises: d2131323d976
Create Date: 2024-05-17 00:52:31.396750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8178fe16853'
down_revision: Union[str, None] = 'd2131323d976'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users', 'password')


def downgrade() -> None:
    pass
