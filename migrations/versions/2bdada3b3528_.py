"""empty message

Revision ID: 2bdada3b3528
Revises: a911fcc93b55
Create Date: 2024-10-07 17:52:19.388629

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2bdada3b3528'
down_revision = 'a911fcc93b55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('hl_tr_data_detail_root_cause_members', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_repair', sa.Boolean(), nullable=True, comment='1=ya, 0=tidak'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hl_tr_data_detail_root_cause_members', schema=None) as batch_op:
        batch_op.drop_column('is_repair')

    with op.batch_alter_table('hl_ms_excel_variables', schema=None) as batch_op:
        batch_op.alter_column('formula',
               existing_type=sa.String(length=255),
               type_=sa.TEXT(),
               existing_comment='Formula name for calculation',
               existing_nullable=True)

    op.create_table('pfi_ms_equipment',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('parent_id', sa.UUID(), autoincrement=False, nullable=True, comment='ref to id table ini sendiri (recursive)'),
    sa.Column('category_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False, comment='Nama Equipment'),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True, comment='Deskripsi Equipment'),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['pfi_ms_category.id'], name='pfi_ms_equipment_category_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['parent_id'], ['pfi_ms_equipment.id'], name='pfi_ms_equipment_parent_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pfi_ms_equipment_pkey')
    )
    op.create_table('pfi_value_tag',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('tag_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('time_stamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('value', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('units_abbreviation', sa.VARCHAR(length=15), autoincrement=False, nullable=False),
    sa.Column('good', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('questionable', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('substituted', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('annotated', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['pfi_ms_tag.id'], name='pfi_value_tag_tag_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='pfi_value_tag_pkey')
    )
    op.create_table('pfi_ms_category',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False, comment='Nama Category'),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pfi_ms_category_pkey')
    )
    op.create_table('pfi_ms_tag',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('web_id', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('path', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('descriptor', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('point_class', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('point_type', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('digital_set_name', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.Column('engineering_units', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('span', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('zero', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('step', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('future', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('display_digits', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pfi_ms_tag_pkey')
    )
    # ### end Alembic commands ###
