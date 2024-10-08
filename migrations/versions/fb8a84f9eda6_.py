"""empty message

Revision ID: fb8a84f9eda6
Revises: 9153a964e600
Create Date: 2024-10-09 14:11:16.924981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb8a84f9eda6'
down_revision = '9153a964e600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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

    # ### end Alembic commands ###
