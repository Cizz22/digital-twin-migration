"""empty message

Revision ID: 0477ca51a61b
Revises: becb70a4e6e4
Create Date: 2024-09-24 16:31:25.621884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0477ca51a61b'
down_revision = 'becb70a4e6e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auth_mr_user', schema=None) as batch_op:
        batch_op.drop_index('users_name_email_username_idx')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('auth_mr_user', schema=None) as batch_op:
        batch_op.create_index('users_name_email_username_idx', ['name', 'email', 'username'], unique=False)

    # ### end Alembic commands ###
