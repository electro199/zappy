"""empty message

Revision ID: 6546c41828df
Revises: 213a40388bf3
Create Date: 2024-04-25 23:08:27.524072

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6546c41828df'
down_revision: Union[str, None] = '213a40388bf3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auto_response_messages', sa.Column('case_sensitive', sa.Boolean(), nullable=True))
    op.add_column('auto_response_messages', sa.Column('enabled', sa.Boolean(), nullable=True))
    op.add_column('auto_response_messages', sa.Column('ephemeral', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('auto_response_messages', 'ephemeral')
    op.drop_column('auto_response_messages', 'enabled')
    op.drop_column('auto_response_messages', 'case_sensitive')
    # ### end Alembic commands ###