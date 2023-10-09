"""Adding new column

Revision ID: d2ce7b6d8d37
Revises: 87f5fe26aef8
Create Date: 2023-10-09 15:12:39.832496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2ce7b6d8d37'
down_revision = '87f5fe26aef8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('songs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.VARCHAR(length=100), nullable=False))

    # ### end Alembic commands ###
