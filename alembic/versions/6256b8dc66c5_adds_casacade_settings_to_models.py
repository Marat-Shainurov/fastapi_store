"""adds casacade settings to models

Revision ID: 6256b8dc66c5
Revises: bd5c93bf6447
Create Date: 2023-09-26 14:02:00.488697

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6256b8dc66c5'
down_revision: Union[str, None] = 'bd5c93bf6447'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
