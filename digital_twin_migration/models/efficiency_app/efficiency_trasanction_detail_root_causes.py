"""
Define the Cases model
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


class EfficiencyDataDetailRootCause(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Cases model"""

    __tablename__ = "hl_tr_data_detail_root_cause"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    data_detail_id = Column(UUID(as_uuid=True), ForeignKey(
        'hl_tr_data_detail.id', ondelete="CASCADE"), nullable=True, comment='Ref to hl_tr_data_detail')
    cause_id = Column(UUID(as_uuid=True), ForeignKey('hl_ms_excel_variables_cause.id',
                      ondelete="CASCADE"), nullable=True, comment='Ref to hl_m_cause 1 to many')
    is_repair = Column(Boolean, default=False, comment='1=ya, 0=tidak')
    is_checked = Column(Boolean, default=False, comment='1=ya, 0=tidak')
    biaya = Column(Float, nullable=True,
                   comment='Besar Biaya yang dikeluarkan (input)')
    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    __mapper_args__ = {"eager_defaults": True}

    variable_cause = relationship(
        "VariableCause", back_populates="root_causes", lazy="joined")
    efficiency_transaction_detail = relationship(
        "EfficiencyDataDetail", back_populates="root_causes", lazy="joined")
    
    actions = relationship("EfficiencyDataDetailRootCauseAction", back_populates="root_cause", lazy="selectin")
