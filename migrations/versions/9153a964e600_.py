"""empty message

Revision ID: 9153a964e600
Revises: 434585cfdaa3
Create Date: 2024-10-09 13:53:42.155353

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "9153a964e600"
down_revision = "434585cfdaa3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("dl_features_data", schema=None) as batch_op:
        batch_op.drop_constraint("dl_features_data_equipment_id_fkey", type_="foreignkey")

    with op.batch_alter_table("dl_predict", schema=None) as batch_op:
        batch_op.drop_constraint("dl_predict_equipment_id_fkey", type_="foreignkey")

    with op.batch_alter_table("rm_pof_predict", schema=None) as batch_op:
        batch_op.drop_constraint("rm_pof_predict_eq_id_fkey", type_="foreignkey")

    op.drop_constraint(
        "equipment_master_equipment_tree_id_fkey", "equipment_master", type_="foreignkey"
    )
    op.drop_table("equipment_tree")
    op.drop_table("equipment_master")

    op.create_table(
        "ms_equipment_tree",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("level_no", sa.Integer(), nullable=False, comment="Level Number"),
        sa.Column("name", sa.String(length=255), nullable=False, comment="Nama Equipment Tree"),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "ms_equipment_master",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column(
            "parent_id", sa.UUID(), nullable=True, comment="ref to id table ini sendiri (recursive)"
        ),
        sa.Column("equipment_tree_id", sa.UUID(), nullable=True),
        sa.Column("category_id", sa.UUID(), nullable=True),
        sa.Column("system_tag", sa.String(length=255), nullable=True, comment="System Tag"),
        sa.Column("assetnum", sa.String(length=255), nullable=True, comment="Asset Number"),
        sa.Column("location_tag", sa.String(length=255), nullable=True, comment="Location Tag"),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["category_id"], ["dl_ms_category.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["equipment_tree_id"], ["ms_equipment_tree.id"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["parent_id"], ["ms_equipment_master.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    with op.batch_alter_table("dl_features_data", schema=None) as batch_op:
        batch_op.create_foreign_key(
            None, "ms_equipment_master", ["equipment_id"], ["id"], ondelete="CASCADE"
        )

    with op.batch_alter_table("dl_predict", schema=None) as batch_op:
        batch_op.create_foreign_key(
            None, "ms_equipment_master", ["equipment_id"], ["id"], ondelete="CASCADE"
        )

    with op.batch_alter_table("rm_pof_predict", schema=None) as batch_op:
        batch_op.alter_column("eq_id", existing_type=sa.UUID(), comment="", existing_nullable=True)
        batch_op.alter_column(
            "risk_class_id", existing_type=sa.UUID(), comment="", existing_nullable=True
        )
        batch_op.create_foreign_key(
            None, "ms_equipment_master", ["eq_id"], ["id"], ondelete="CASCADE"
        )

    with op.batch_alter_table("rm_risk_classification", schema=None) as batch_op:
        batch_op.alter_column(
            "likelihood_id", existing_type=sa.UUID(), comment="", existing_nullable=True
        )
        batch_op.alter_column(
            "severity_id", existing_type=sa.UUID(), comment="", existing_nullable=True
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("rm_risk_classification", schema=None) as batch_op:
        batch_op.alter_column(
            "severity_id",
            existing_type=sa.UUID(),
            comment=None,
            existing_comment="",
            existing_nullable=True,
        )
        batch_op.alter_column(
            "likelihood_id",
            existing_type=sa.UUID(),
            comment=None,
            existing_comment="",
            existing_nullable=True,
        )

    with op.batch_alter_table("rm_pof_predict", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "rm_pof_predict_eq_id_fkey", "equipment_master", ["eq_id"], ["id"], ondelete="CASCADE"
        )
        batch_op.alter_column(
            "risk_class_id",
            existing_type=sa.UUID(),
            comment=None,
            existing_comment="",
            existing_nullable=True,
        )
        batch_op.alter_column(
            "eq_id",
            existing_type=sa.UUID(),
            comment=None,
            existing_comment="",
            existing_nullable=True,
        )

    with op.batch_alter_table("dl_predict", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "dl_predict_equipment_id_fkey",
            "equipment_master",
            ["equipment_id"],
            ["id"],
            ondelete="CASCADE",
        )

    with op.batch_alter_table("dl_features_data", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "dl_features_data_equipment_id_fkey",
            "equipment_master",
            ["equipment_id"],
            ["id"],
            ondelete="CASCADE",
        )

    op.create_table(
        "equipment_master",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "parent_id",
            sa.UUID(),
            autoincrement=False,
            nullable=True,
            comment="ref to id table ini sendiri (recursive)",
        ),
        sa.Column("equipment_tree_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column(
            "system_tag",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
            comment="System Tag",
        ),
        sa.Column(
            "assetnum",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
            comment="Asset Number",
        ),
        sa.Column(
            "location_tag",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
            comment="Location Tag",
        ),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("category_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["dl_ms_category.id"],
            name="equipment_master_category_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["equipment_tree_id"],
            ["equipment_tree.id"],
            name="equipment_master_equipment_tree_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["equipment_master.id"],
            name="equipment_master_parent_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="equipment_master_pkey"),
    )
    op.create_table(
        "equipment_tree",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column(
            "equipment_tree_id",
            sa.UUID(),
            autoincrement=False,
            nullable=True,
            comment="ref to id table ini sendiri (recursive)",
        ),
        sa.Column(
            "level_no", sa.INTEGER(), autoincrement=False, nullable=False, comment="Level Number"
        ),
        sa.Column(
            "name",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=False,
            comment="Nama Equipment Tree",
        ),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["equipment_tree_id"],
            ["equipment_tree.id"],
            name="equipment_tree_equipment_tree_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="equipment_tree_pkey"),
    )
    op.drop_table("ms_equipment_master")
    op.drop_table("ms_equipment_tree")
    # ### end Alembic commands ###
