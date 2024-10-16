"""empty message

Revision ID: 73db4645f414
Revises: b3d2ff2d7d18
Create Date: 2024-10-14 16:05:49.122168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73db4645f414'
down_revision = 'b3d2ff2d7d18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.add_column(sa.Column('good_indicator', sa.String(length=25), nullable=True, comment='Plus, Minus, Equal'))

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

    with op.batch_alter_table('hl_tr_data_detail', schema=None) as batch_op:
        batch_op.create_index('hl_tr_data_detail_efficiency_transaction_id_idx', ['efficiency_transaction_id', 'variable_id'], unique=True)

    with op.batch_alter_table('hl_tr_data', schema=None) as batch_op:
        batch_op.create_index('hl_tr_data_name_idx', ['name'], unique=False)

    with op.batch_alter_table('hl_ms_excel_variables_cause', schema=None) as batch_op:
        batch_op.create_index('hl_ms_excel_variables_cause_id_idx', ['id', 'parent_id', 'variable_id'], unique=True)

    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.create_index('hl_ms_excel_variables_excel_variable_name_idx', ['excel_variable_name', 'in_out', 'excel_id'], unique=True)
        batch_op.drop_column('good_indicator')

    # ### end Alembic commands ###
