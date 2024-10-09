from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class RMPofPredict(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "rm_pof_predict"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    year = db.Column(db.Integer, nullable=True, comment="pof predict year")
    value = db.Column(db.Double, nullable=True, comment="pof predict value")
    eq_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("ms_equipment_master.id", ondelete="CASCADE"),
        nullable=True,
        comment="",
    )
    risk_class_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("rm_risk_classification.id", ondelete="CASCADE"),
        nullable=True,
        comment="",
    )

    equipment = relationship("PFIEquipment", back_populates="pof_predicts", lazy="joined")
    risk_classification = relationship(
        "RMRiskClassification", back_populates="pof_predicts", lazy="joined"
    )

    __mapper_args__ = {"eager_defaults": True}
