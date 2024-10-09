from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class RMMasterLikelihood(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "rm_master_likelihood"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = db.Column(db.String(50), nullable=True, comment="master data likelihood name")

    risk_classifications = relationship("RMRiskClassification", back_populates="master_likelihood", lazy="selectIn")

    __mapper_args__ = {"eager_defaults": True}
