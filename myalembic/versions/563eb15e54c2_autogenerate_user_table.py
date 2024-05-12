"""autogenerate user table

Revision ID: 563eb15e54c2
Revises:
Create Date: 2024-05-12 13:41:20.639223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '563eb15e54c2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('password', sa.String)

    )  

def downgrade():
    op.drop_table('user')
