"""empty message

Revision ID: 7f05bf45aef6
Revises: 29ff925f9f6e
Create Date: 2024-08-19 12:18:49.612512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f05bf45aef6'
down_revision = '29ff925f9f6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_id', sa.UUID(), nullable=False))
        batch_op.create_foreign_key(None, 'roles', ['role_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('role_id')

    # ### end Alembic commands ###
