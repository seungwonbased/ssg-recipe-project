"""empty message

Revision ID: 802d546d6333
Revises: 1b30edc0db40
Create Date: 2023-09-02 00:00:55.522282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '802d546d6333'
down_revision = '1b30edc0db40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), server_default='1', nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_post_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_post_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
