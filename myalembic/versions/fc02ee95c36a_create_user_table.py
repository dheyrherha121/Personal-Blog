"""create user table

Revision ID: fc02ee95c36a
Revises: 563eb15e54c2
Create Date: 2024-05-12 14:00:15.171868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc02ee95c36a'
down_revision: Union[str, None] = '563eb15e54c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String)

    )


def downgrade() -> None:
    op.drop_table('users')
