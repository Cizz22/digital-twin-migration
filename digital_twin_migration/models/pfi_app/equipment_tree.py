from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIEquipmentTree(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "ms_equipment_tree"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    level_no = db.Column(db.Integer, nullable=False, comment="Level Number")
    name = db.Column(db.String(255), nullable=False, comment="Nama Equipment Tree")

    equipments = relationship("PFIEquipment", back_populates="equipment_tree", lazy="selectin")

    __mapper_args__ = {"eager_defaults": True}
