from __future__ import annotations

from .Database import Base
from .enums.StatusEnum import Status
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from sqlalchemy import Enum as SQEnum

if TYPE_CHECKING:
    from .WorkOrder import WorkOrder


class Vehicle(Base):
    __tablename__: str = "vehicles"

    primary_key: Mapped[int] = mapped_column(primary_key=True)
    vin: Mapped[str] = mapped_column(String(17))
    name: Mapped[str] = mapped_column(String(50))
    make: Mapped[str] = mapped_column(String(40))
    model: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(Integer)
    status: Mapped[Status] = mapped_column(SQEnum(Status), default=Status.ACTIVE)

    workorders: Mapped[list["WorkOrder"]] = relationship(
        back_populates="vehicle", cascade="all, delete-orphan"
    )
