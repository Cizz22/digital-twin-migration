"""empty message

Revision ID: e688825423c1
Revises: 7f993aeaf5fd
Create Date: 2024-09-26 16:51:11.220969

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "e688825423c1"
down_revision = "7f993aeaf5fd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("hl_ms_masterdata", schema=None) as batch_op:
        batch_op.alter_column("updated_at", existing_type=postgresql.TIMESTAMP(), nullable=False)

    # Drop `pfi_value_tag` table
    op.drop_table("pfi_value_tag")

    # Drop `pfi_ms_tag` table
    op.drop_table("pfi_ms_tag")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("pfi_value_tag", schema=None) as batch_op:
        batch_op.alter_column(
            "tag_id",
            existing_type=sa.BigInteger(),
            type_=sa.UUID(),
            nullable=True,
            comment="ref to id table ini sendiri (recursive)",
        )

    with op.batch_alter_table("pfi_ms_tag", schema=None) as batch_op:
        batch_op.alter_column(
            "id",
            existing_type=sa.BigInteger(),
            type_=sa.UUID(),
            existing_nullable=False,
            autoincrement=True,
        )

    with op.batch_alter_table("hl_ms_masterdata", schema=None) as batch_op:
        batch_op.alter_column("updated_at", existing_type=postgresql.TIMESTAMP(), nullable=True)
