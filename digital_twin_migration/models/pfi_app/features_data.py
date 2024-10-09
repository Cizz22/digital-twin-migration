from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIFeaturesData(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_features_data"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    equipment_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("equipment_master.id", ondelete="CASCADE"),
        nullable=True,
        comment="ref to id table ini sendiri (recursive)",
    )

    features_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("dl_ms_features.id", ondelete="CASCADE"),
        nullable=True,
    )

    date_time = db.Column(db.DateTime, nullable=True, comment="Date Time")
    value = db.Column(db.Float, nullable=True, comment="Value")

    equipment = relationship("PFIEquipment", back_populates="features_data", lazy="joined")
    feature = relationship("PFIFeature", back_populates="features_data", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
