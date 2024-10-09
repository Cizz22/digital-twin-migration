from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class RMRiskClassification(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "rm_risk_classification"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    risk_class = db.Column(db.String(100), nullable=True, comment="class")
    likelihood_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("rm_master_likelihood.id", ondelete="CASCADE"),
        nullable=True,
        comment="",
    )
    severity_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("rm_master_severity.id", ondelete="CASCADE"),
        nullable=True,
        comment="",
    )

    pof_predicts = relationship(
        "RMPofPredict", back_populates="risk_classification", lazy="selectin"
    )

    master_likelihood = relationship(
        "RMMasterLikelihood", back_populates="risk_classifications", lazy="joined"
    )
    master_severity = relationship(
        "RMMasterSeverity", back_populates="risk_classifications", lazy="joined"
    )

    __mapper_args__ = {"eager_defaults": True}
