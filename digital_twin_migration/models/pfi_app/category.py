from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFICategory(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_ms_category"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(255), nullable=True, comment="Nama Category")
    rigid_or_flexy = db.Column(db.Boolean, nullable=True, comment="Rigid or Flexy")
    edges_a = db.Column(db.Integer, nullable=True, comment="Edges A")
    edges_b = db.Column(db.Integer, nullable=True, comment="Edges B")
    edges_c = db.Column(db.Integer, nullable=True, comment="Edges C")
    edges_d = db.Column(db.Integer, nullable=True, comment="Edges D")

    equipments = relationship("PFIEquipment", back_populates="category", lazy="selectin")
