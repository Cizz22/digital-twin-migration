
"""
Define the Variable Causes model
"""
from enum import Enum
from uuid import uuid4

from sqlalchemy import JSON, BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
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


class VariableCause(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Variable Causes model"""

    __tablename__ = "hl_ms_excel_variables_cause"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('hl_ms_excel_variables_cause.id'),
                       nullable=True, comment='ref to id table ini sendiri (recursive)')
    variable_id = Column(UUID(as_uuid=True), ForeignKey(
        'hl_ms_excel_variables.id', ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=True)
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)

    parent = relationship("VariableCause", remote_side=[id], backref="children")
    root_cause_members = relationship("EfficiencyDataDetailRootCauseMember", back_populates="variable_cause", lazy="raise")
    root_causes = relationship("EfficiencyDataDetailRootCause", back_populates="parent_cause", lazy="raise")
    variable = relationship("Variable", back_populates="causes", lazy="raise")
    actions = relationship("VariableCauseAction", back_populates="cause", lazy="raise")
    __mapper_args__ = {"eager_defaults": True}
