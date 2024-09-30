"""empty message

Revision ID: fd909fe01f21
Revises: a48bbd4928aa
Create Date: 2024-09-30 17:26:52.519452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd909fe01f21'
down_revision = 'a48bbd4928aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.add_column(sa.Column('konstanta', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.drop_column('konstanta')

    # ### end Alembic commands ###
