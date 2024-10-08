"""
Define the Cases model
"""

from enum import Enum
from uuid import uuid4

from sqlalchemy import (
    JSON,
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)


class EfficiencyDataDetailRootCauseAction(
    db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel
):
    """The Cause Action TR model"""

    __tablename__ = "hl_tr_data_detail_root_cause_actions"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    action_id = Column(
        UUID(as_uuid=True),
        ForeignKey("hl_ms_excel_variables_cause_actions.id", ondelete="CASCADE"),
        nullable=True,
    )
    root_cause_id = Column(
        UUID(as_uuid=True),
        ForeignKey("hl_tr_data_detail_root_cause.id", ondelete="CASCADE"),
        nullable=True,
    )
    is_checked = Column(Boolean, default=False)
    biaya = Column(Float, nullable=True, comment="Besar Biaya yang dikeluarkan (input)")
    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    __mapper_args__ = {"eager_defaults": True}

    action = relationship("VariableCauseAction", back_populates="root_cause_actions", lazy="joined")
    root_cause = relationship(
        "EfficiencyDataDetailRootCause", back_populates="actions", lazy="joined"
    )
