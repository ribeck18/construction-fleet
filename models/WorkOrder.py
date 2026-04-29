from __future__ import annotations

from models.Inspection import Inspection
from .Database import Base
from .enums.SeverityEnum import SeverityEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, Date
from sqlalchemy import Enum as SAEnum
from datetime import datetime, date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .Vehicle import Vehicle


class WorkOrder(Base):
    __tablename__: str = "workorders"

    primary_key: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    severity: Mapped[SeverityEnum] = mapped_column(SAEnum(SeverityEnum))
    description: Mapped[str] = mapped_column(String(500))
    photo_path: Mapped[str] = mapped_column(String())
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    resolved_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    due_date: Mapped[date] = mapped_column(Date, nullable=True)

    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.primary_key"))
    vehicle: Mapped["Vehicle"] = relationship(back_populates="workorders")

    inspection: Mapped["Inspection"] = relationship(back_populates="workorder")
