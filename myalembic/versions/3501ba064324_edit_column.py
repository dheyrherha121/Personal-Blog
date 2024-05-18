"""edit column

Revision ID: 3501ba064324
Revises: 5bfeddc2bf6a
Create Date: 2024-05-17 00:21:48.650916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3501ba064324'
down_revision: Union[str, None] = '5bfeddc2bf6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('users', 'password')


def downgrade() -> None:
    pass
