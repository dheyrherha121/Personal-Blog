from sqlalchemy.sql.expression import text
"""create new table

Revision ID: fd7309a9c924
Revises: 5e56cd94d133
Create Date: 2024-05-16 23:24:45.650830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd7309a9c924'
down_revision: Union[str, None] = '5e56cd94d133'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.INTEGER, nullable=True, primary_key=True, autoincrement=True),
                    sa.Column('email', sa.VARCHAR, nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')),
                    sa.Column('password', sa.VARCHAR, nullable=False))


def downgrade() -> None:
    op.drop_table('users')
