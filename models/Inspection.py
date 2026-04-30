from __future__ import annotations

from .Database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Boolean, ForeignKey, Integer, String, DateTime
from sqlalchemy import Enum as SQEnum
from .enums.QuestionTypesEnum import QuestionTypesEnum
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.Vehicle import Vehicle
    from models.WorkOrder import WorkOrder


class InspectionQuestion(Base):
    __tablename__ = "inspection_questions"

    primary_key: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    question_type: Mapped[QuestionTypesEnum] = mapped_column(SQEnum(QuestionTypesEnum))

    inspection_items: Mapped[list["InspectionItem"]] = relationship(
        back_populates="question"
    )


class InspectionItem(Base):
    __tablename__ = "inspection_items"

    primary_key: Mapped[int] = mapped_column(primary_key=True)
    is_passed: Mapped[bool] = mapped_column(Boolean, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)

    question_id: Mapped[int] = mapped_column(
        ForeignKey("inspection_questions.primary_key")
    )
    inspection_id: Mapped[int] = mapped_column(ForeignKey("inspections.primary_key"))

    inspection: Mapped["Inspection"] = relationship(back_populates="inspection_items")
    question: Mapped["InspectionQuestion"] = relationship(
        back_populates="inspection_items"
    )


class Inspection(Base):
    __tablename__ = "inspections"

    primary_key: Mapped[int] = mapped_column(primary_key=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.primary_key"))
    date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    vehicle: Mapped["Vehicle"] = relationship(back_populates="inspections")
    inspection_items: Mapped[list["InspectionItem"]] = relationship(
        back_populates="inspection", cascade="all, delete-orphan"
    )


# This is old the inspection class for reference:
# # Basic Data
# primary_key: Mapped[int] = mapped_column(primary_key=True)
# name: Mapped[str] = mapped_column(String(30))
# created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
# current_mileage: Mapped[int] = mapped_column(Integer)
#
# # Safety/critical data
# brakes_bad: Mapped[bool] = mapped_column(Boolean)
# brakes_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# park_brake_fail: Mapped[bool] = mapped_column(Boolean)
# park_brake_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# steering_issues: Mapped[bool] = mapped_column(Boolean)
# steering_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# lights_out: Mapped[bool] = mapped_column(Boolean)
# lights_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# signals_out: Mapped[bool] = mapped_column(Boolean)
# signals_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# mirrors_broken: Mapped[bool] = mapped_column(Boolean)
# mirrors_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# windshield_broken: Mapped[bool] = mapped_column(Boolean)
# windshield_desc: Mapped[str | None] = mapped_column(String, nullable=True)
#
# # Mechanical
# oil_level_low: Mapped[bool] = mapped_column(Boolean)
# oil_level_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# coolant_level_low: Mapped[bool] = mapped_column(Boolean)
# coolant_level_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# leaks: Mapped[bool] = mapped_column(Boolean)
# leaks_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# trans_fluid_level_low: Mapped[bool] = mapped_column(Boolean)
# trans_fluid_level_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# bad_battery: Mapped[bool] = mapped_column(Boolean)
# battery_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# warning_lights: Mapped[bool] = mapped_column(Boolean)
# warning_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# poor_tire_pressure: Mapped[bool] = mapped_column(Boolean)
# tire_pressure_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# poor_tread_depth: Mapped[bool] = mapped_column(Boolean)
# tread_depth_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# tire_damage: Mapped[bool] = mapped_column(Boolean)
# tire_damage_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# missing_lug_nuts: Mapped[bool] = mapped_column(Boolean)
# lug_nuts_desc: Mapped[str | None] = mapped_column(String, nullable=True)
#
# # Damage/wear
# exterior_damage: Mapped[bool] = mapped_column(Boolean)
# exterior_damage_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# interior_damage: Mapped[bool] = mapped_column(Boolean)
# interior_damag_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# excessive_wear: Mapped[bool] = mapped_column(Boolean)
# excessive_wear_desc: Mapped[str | None] = mapped_column(String, nullable=True)
#
# # Operation Check
# starting_issues: Mapped[bool] = mapped_column(Boolean)
# starting_issues_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# unusual_noise: Mapped[bool] = mapped_column(Boolean)
# unusual_noise_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# excessive_smoke: Mapped[bool] = mapped_column(Boolean)
# excessive_smoke_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# rough_transmission: Mapped[bool] = mapped_column(Boolean)
# rough_transmission_desc: Mapped[str | None] = mapped_column(String, nullable=True)
#
# # Documents
# registration_expired: Mapped[bool] = mapped_column(Boolean)
# no_insurance_card: Mapped[bool] = mapped_column(Boolean)
#
# # Safety Equipment
# horn_failure: Mapped[bool] = mapped_column(Boolean)
# horn_failure_desc: Mapped[bool] = mapped_column(Boolean)
# backup_alarm_failure: Mapped[bool] = mapped_column(Boolean)
# backup_alarm_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# seatbelt_failure: Mapped[bool] = mapped_column(Boolean)
# seatbelt_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# fire_extinguisher_old_missing: Mapped[bool] = mapped_column(Boolean)
# fire_extinguisher_desc: Mapped[str | None] = mapped_column(String, nullable=True)
# missing_safety_gear: Mapped[bool] = mapped_column(Boolean)
# missing_safety_gear_desc: Mapped[str | None] = mapped_column(String, nullable=True)
#
# # Relationships
# vehicle_id: Mapped[int] = mapped_column(ForeignKey("vehicles.primary_key"))
# vehicle: Mapped["Vehicle"] = relationship(back_populates="inspections")
#
# workorder_id: Mapped[int] = mapped_column(ForeignKey("workorders.primary_key"))
# workorder: Mapped["WorkOrder"] = relationship(back_populates="inspection")
