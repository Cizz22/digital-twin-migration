"""empty message

Revision ID: 93b69fa3835e
Revises: 83bf2232ad79
Create Date: 2024-10-12 16:43:02.961529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93b69fa3835e'
down_revision = '83bf2232ad79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.add_column(sa.Column('condensor_value', sa.Float(), nullable=True))

    with op.batch_alter_table('rm_pof_predict', schema=None) as batch_op:
        batch_op.alter_column('eq_id',
               existing_type=sa.UUID(),
               comment='',
               existing_nullable=True)
        batch_op.alter_column('risk_class_id',
               existing_type=sa.UUID(),
               comment='',
               existing_nullable=True)

    with op.batch_alter_table('rm_risk_classification', schema=None) as batch_op:
        batch_op.alter_column('likelihood_id',
               existing_type=sa.UUID(),
               comment='',
               existing_nullable=True)
        batch_op.alter_column('severity_id',
               existing_type=sa.UUID(),
               comment='',
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rm_risk_classification', schema=None) as batch_op:
        batch_op.alter_column('severity_id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='',
               existing_nullable=True)
        batch_op.alter_column('likelihood_id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='',
               existing_nullable=True)

    with op.batch_alter_table('rm_pof_predict', schema=None) as batch_op:
        batch_op.alter_column('risk_class_id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='',
               existing_nullable=True)
        batch_op.alter_column('eq_id',
               existing_type=sa.UUID(),
               comment=None,
               existing_comment='',
               existing_nullable=True)

    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.drop_column('condensor_value')

    # ### end Alembic commands ###
