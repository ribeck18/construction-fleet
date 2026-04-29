from __future__ import annotations
from datetime import datetime
from .Database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey, Integer, String, DateTime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Vehicle import Vehicle
    from models.WorkOrder import WorkOrder


class Inspection(Base):
    __tablename__ = "inspections"

    # Basic Data
    primary_key: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    current_mileage: Mapped[int] = mapped_column(Integer)

    # Safety/critical data
    brakes_bad: Mapped[bool] = mapped_column(Boolean)
    park_brake_fail: Mapped[bool] = mapped_column(Boolean)
    steering_issues: Mapped[bool] = mapped_column(Boolean)
    lights_out: Mapped[bool] = mapped_column(Boolean)
    signals_out: Mapped[bool] = mapped_column(Boolean)
    mirrors_broken: Mapped[bool] = mapped_column(Boolean)
    windshield_broken: Mapped[bool] = mapped_column(Boolean)

    # Mechanical
    oil_level_low: Mapped[bool] = mapped_column(Boolean)
    coolant_level_low: Mapped[bool] = mapped_column(Boolean)
    leaks: Mapped[bool] = mapped_column(Boolean)
    trans_fluid_level_low: Mapped[bool] = mapped_column(Boolean)
    bad_battery: Mapped[bool] = mapped_column(Boolean)
    warning_lights: Mapped[bool] = mapped_column(Boolean)
    poor_tire_pressure: Mapped[bool] = mapped_column(Boolean)
    poor_tread_depth: Mapped[bool] = mapped_column(Boolean)
    tire_damage: Mapped[bool] = mapped_column(Boolean)
    missing_lug_nuts: Mapped[bool] = mapped_column(Boolean)

    # Damage/wear
    exterior_damage: Mapped[bool] = mapped_column(Boolean)
    interior_damage: Mapped[bool] = mapped_column(Boolean)
    excessive_wear: Mapped[bool] = mapped_column(Boolean)

    # Operation Check
    starting_issues: Mapped[bool] = mapped_column(Boolean)
    unusual_noise: Mapped[bool] = mapped_column(Boolean)
    excessive_smoke: Mapped[bool] = mapped_column(Boolean)
    rough_transmission: Mapped[bool] = mapped_column(Boolean)

    # Documents
    registration_expired: Mapped[bool] = mapped_column(Boolean)
    no_insurance_card: Mapped[bool] = mapped_column(Boolean)

    # Safety Equipment
    horn_failur: Mapped[bool] = mapped_column(Boolean)
    backup_alarm_failure: Mapped[bool] = mapped_column(Boolean)
    seatbelt_failure: Mapped[bool] = mapped_column(Boolean)
    fire_extinguisher_old_missing: Mapped[bool] = mapped_column(Boolean)
    missing_safety_gea: Mapped[bool] = mapped_column(Boolean)

    # Relationships
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.primary_key"))
    vehicle: Mapped["Vehicle"] = relationship(back_populates="inspections")

    workorder_id: Mapped[int] = mapped_column(ForeignKey("workorders.primary_key"))
    workorder: Mapped["WorkOrder"] = relationship(back_populates="inspection")
