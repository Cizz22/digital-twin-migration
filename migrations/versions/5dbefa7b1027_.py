"""empty message

Revision ID: 5dbefa7b1027
Revises: 9bf64f18f7fe
Create Date: 2024-09-27 13:44:06.683223

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dbefa7b1027'
down_revision = '9bf64f18f7fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('unique_id', sa.String(length=300), nullable=True))
        batch_op.create_unique_constraint(None, ['unique_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('unique_id')

    # ### end Alembic commands ###
