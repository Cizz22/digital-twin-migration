from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIEquipment(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "equipment_master"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("equipment_master.id", ondelete="CASCADE"),
        nullable=True,
        comment="ref to id table ini sendiri (recursive)",
    )
    equipment_tree_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("equipment_tree.id", ondelete="CASCADE"),
        nullable=True,
        comment="ref to id table ini sendiri (recursive)",
    )

    system_tag = db.Column(db.String(255), nullable=True, comment="System Tag")
    assetnum = db.Column(db.String(255), nullable=True, comment="Asset Number")
    location_tag = db.Column(db.String(255), nullable=True, comment="Location Tag")

    parent = relationship("PFIEquipment", remote_side=[id], backref="children")
    equipment_tree = relationship("PFIEquipmentTree", back_populates="equipments", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
