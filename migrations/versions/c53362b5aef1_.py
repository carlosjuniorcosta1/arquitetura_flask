"""empty message

Revision ID: c53362b5aef1
Revises: 97de42caa73b
Create Date: 2024-02-28 19:42:33.605936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c53362b5aef1'
down_revision = '97de42caa73b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('breed', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('puppies', schema=None) as batch_op:
        batch_op.drop_column('breed')

    # ### end Alembic commands ###