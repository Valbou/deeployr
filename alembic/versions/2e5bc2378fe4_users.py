"""users

Revision ID: 2e5bc2378fe4
Revises: 
Create Date: 2024-03-23 13:30:46.544137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.colors.persistence.sqlalchemy.color import ColorType
from src.users.persistence.sqlalchemy.tables.right_table import PermissionsType
from src.users.persistence.sqlalchemy.tables.user_table import LocaleField


# revision identifiers, used by Alembic.
revision: str = '2e5bc2378fe4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

requesttype_enum = sa.Enum("RequestType.EMAIL", "RequestType.PASSWORD", name="requesttype")
resources_enum = sa.Enum("Resources.GROUP", "Resources.ROLE", "Resources.ROLETYPE", name="resources")

def upgrade() -> None:
    op.create_table(
        "groups",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "requestschanges",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            "request_type",
            requesttype_enum,
            nullable=False,
        ),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("code", sa.String(length=12), nullable=False),
        sa.Column("done", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(length=25), nullable=False),
        sa.Column("last_name", sa.String(length=25), nullable=False),
        sa.Column("email", sa.String(length=250), nullable=False),
        sa.Column("hash_password", sa.String(length=256), nullable=True),
        sa.Column("locale", LocaleField(length=20), nullable=True),
        sa.Column("timezone", sa.String(length=35), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("last_login_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "roletypes",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("group_id", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["groups.id"],
            name="fk_roletypes_group_id",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "group_id", name="roletype_name_group"),
    )
    op.create_index(
        "roletype_name_group_index", "roletypes", ["name", "group_id"], unique=False
    )
    op.create_table(
        "tokens",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("last_activity_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("temp", sa.Boolean(), nullable=False),
        sa.Column("temp_code", sa.String(length=12), nullable=True),
        sa.Column("sha_token", sa.String(length=64), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_tokens_user_id", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("sha_token"),
    )
    op.create_table(
        "rights",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("roletype_id", sa.String(), nullable=False),
        sa.Column("resource", resources_enum, nullable=False),
        sa.Column("permissions", PermissionsType(), nullable=False),
        sa.ForeignKeyConstraint(
            ["roletype_id"],
            ["roletypes.id"],
            name="fk_rights_roletype_id",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("roletype_id", "resource", name="right_roletype_resource"),
    )
    op.create_index(
        "right_roletype_resource_index",
        "rights",
        ["roletype_id", "resource"],
        unique=False,
    )
    op.create_table(
        "roles",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("user_id", sa.String(), nullable=False),
        sa.Column("group_id", sa.String(), nullable=False),
        sa.Column("roletype_id", sa.String(), nullable=False),
        sa.Column("color", ColorType(length=20), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_id"], ["groups.id"], name="fk_roles_group_id", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["roletype_id"],
            ["roletypes.id"],
            name="fk_roles_roletype_id",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_roles_user_id", ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id", "group_id", name="role_user_group"),
    )
    op.create_index(
        "role_user_group_index", "roles", ["user_id", "group_id"], unique=False
    )


def downgrade() -> None:
    op.drop_index("role_user_group_index", table_name="roles")
    op.drop_table("roles")
    op.drop_index("right_roletype_resource_index", table_name="rights")
    op.drop_table("rights")
    op.drop_table("tokens")
    op.drop_index("roletype_name_group_index", table_name="roletypes")
    op.drop_table("roletypes")
    op.drop_table("users")
    op.drop_table("requestschanges")
    op.drop_table("groups")
    requesttype_enum.drop(op.get_bind(), checkfirst=False)
    resources_enum.drop(op.get_bind(), checkfirst=False)
