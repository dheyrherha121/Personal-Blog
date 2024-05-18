"""create blog table

Revision ID: 5bfeddc2bf6a
Revises: fd7309a9c924
Create Date: 2024-05-16 23:45:49.285843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5bfeddc2bf6a'
down_revision: Union[str, None] = 'fd7309a9c924'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Blogs',
                    sa.Column('id',sa.INTEGER(), primary_key=True, nullable=False, autoincrement=True),
                    sa.Column('content', sa.VARCHAR(), nullable=False),
                    sa.Column('title', sa.VARCHAR(), nullable=False),
                    sa.Column('owner_id', sa.INTEGER(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='Blogs', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')



def downgrade() -> None:
    op.drop_column('users', 'password')
