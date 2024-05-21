"""create article number

Revision ID: dfdf7ea218f3
Revises: c405427f98bc
Create Date: 2024-05-21 11:24:39.675581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfdf7ea218f3'
down_revision: Union[str, None] = 'c405427f98bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('Blogs', sa.Column('Article number', sa.INTEGER(), nullable=False))


def downgrade() -> None:
    pass
