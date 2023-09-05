"""empty message

Revision ID: 8e784b37271b
Revises: 43922a66f76e
Create Date: 2023-09-05 09:39:23.071082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e784b37271b'
down_revision = '43922a66f76e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.drop_column('food_category')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.add_column(sa.Column('food_category', sa.VARCHAR(length=150), nullable=True))

    # ### end Alembic commands ###
