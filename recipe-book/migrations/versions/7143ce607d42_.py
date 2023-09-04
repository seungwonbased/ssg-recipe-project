"""empty message

Revision ID: 7143ce607d42
Revises: 81746abbde01
Create Date: 2023-09-04 15:57:40.372239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7143ce607d42'
down_revision = '81746abbde01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.add_column(sa.Column('foodname', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('unit', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('food_category_name', sa.String(length=150), nullable=False))
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=150),
               nullable=False)
        batch_op.create_unique_constraint(batch_op.f('uq_food_foodname'), ['foodname'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_food_foodname'), type_='unique')
        batch_op.alter_column('price',
               existing_type=sa.String(length=150),
               type_=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('food_category_name')
        batch_op.drop_column('unit')
        batch_op.drop_column('foodname')

    # ### end Alembic commands ###
