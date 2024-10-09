from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIFeature(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_ms_features"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = db.Column(db.String(255), nullable=False, comment="Nama Equipment Tree")
    category = db.Column(db.String(255), nullable=False, comment="Nama Category")

    features_data = relationship("PFIFeaturesData", back_populates="feature", lazy="selectin")
    predicts = relationship("PFIPredict", back_populates="feature", lazy="selectin")

    __mapper_args__ = {"eager_defaults": True}
