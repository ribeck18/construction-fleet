from datetime import datetime
from models.Inspection import Inspection
from pydantic_schemas import InspectionSchema
from pydantic_schemas.InspectionSchema import ReadInspection
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from models.WorkOrder import WorkOrder
from models.enums.SeverityEnum import SeverityEnum
from services.workorder_services import create_workorder


def convert_to_readinspection(inspection: Inspection) -> ReadInspection:
    return ReadInspection.model_validate(inspection)


def get_inspections(session: Session) -> list[Inspection]:
    stmt = select(Inspection)
    inspections = list(session.execute(stmt).scalars().all())
    return inspections


def get_inspection(session: Session, id: int) -> Inspection | None:
    stmt = select(Inspection).where(Inspection.primary_key == id)
    vehicle = session.execute(stmt).scalars().first()

    return vehicle


def get_issues(inspection: Inspection) -> list[str]:
    problems: list[str] = []
    for name, value in inspection.__dict__.items():  # pyright: ignore[reportAny]
        if value is False:
            problems.append(name)

    return problems


def initiate_new_workorder(
    session: Session,
    problem: str,
    inspection: Inspection,
    severity: SeverityEnum,
    description: str,
    photo_path: str,
) -> WorkOrder:
    vehicle_id = inspection.vehicle_id

    workorder: WorkOrder = create_workorder(
        session, problem, severity, description, photo_path, vehicle_id
    )

    return workorder


def create_inspection(
    session: Session,
    name: str,
    created_date: datetime,
    current_mileage: int,
    brakes_bad: bool,
    brakes_desc: str | None,
    park_brake_fail: bool,
    park_brake_desc: str | None,
    steering_issues: bool,
    steering_desc: str | None,
    lights_out: bool,
    lights_desc: str | None,
    signals_out: bool,
    signals_desc: str | None,
    mirrors_broken: bool,
    mirrors_desc: str | None,
    windshield_broken: bool,
    windshield_desc: str | None,
    oil_level_low: bool,
    oil_level_desc: str | None,
    coolant_level_low: bool,
    coolant_level_desc: str | None,
    leaks: bool,
    leaks_desc: str | None,
    trans_fluid_level_low: bool,
    trans_fluid_level_desc: str | None,
    bad_battery: bool,
    battery_desc: str | None,
    warning_lights: bool,
    warning_desc: str | None,
    poor_tire_pressure: bool,
    tire_pressure_desc: str | None,
    poor_tread_depth: bool,
    tread_depth_desc: str | None,
    tire_damage: bool,
    tire_damage_desc: str | None,
    missing_lug_nuts: bool,
    lug_nuts_desc: str | None,
    exterior_damage: bool,
    exterior_damage_desc: str | None,
    interior_damage: bool,
    interior_damag_desc: str | None,
    excessive_wear: bool,
    excessive_wear_desc: str | None,
    starting_issues: bool,
    starting_issues_desc: str | None,
    unusual_noise: bool,
    unusual_noise_desc: str | None,
    excessive_smoke: bool,
    excessive_smoke_desc: str | None,
    rough_transmission: bool,
    rough_transmission_desc: str | None,
    registration_expired: bool,
    no_insurance_card: bool,
    horn_failure: bool,
    horn_failure_desc: str | None,
    backup_alarm_failure: bool,
    backup_alarm_desc: str | None,
    seatbelt_failure: bool,
    seatbelt_desc: str,
    fire_extinguisher_old_missing: bool,
    fire_extinguisher_desc: str | None,
    missing_safety_gear: bool,
    missing_safety_gear_desc: str | None,
    vehicle_id: int,
    workorder_id: int,
) -> Inspection:
    inspection: Inspection = Inspection(
        name=name,
        created_date=created_date,
        current_mileage=current_mileage,
        brakes_bad=brakes_bad,
        brakes_desc=brakes_desc,
        park_brake_fail=park_brake_fail,
        park_brake_desc=park_brake_desc,
        steering_issues=steering_issues,
        steering_desc=steering_desc,
        lights_out=lights_out,
        lights_desc=lights_desc,
        signals_out=signals_out,
        signals_desc=signals_desc,
        mirrors_broken=mirrors_broken,
        mirrors_desc=mirrors_desc,
        windshield_broken=windshield_broken,
        windshield_desc=windshield_desc,
        oil_level_low=oil_level_low,
        oil_level_desc=oil_level_desc,
        coolant_level_low=coolant_level_low,
        coolant_level_desc=coolant_level_desc,
        leaks=leaks,
        leaks_desc=leaks_desc,
        trans_fluid_level_low=trans_fluid_level_low,
        trans_fluid_level_desc=trans_fluid_level_desc,
        bad_battery=bad_battery,
        battery_desc=battery_desc,
        warning_lights=warning_lights,
        warning_desc=warning_desc,
        poor_tire_pressure=poor_tire_pressure,
        tire_pressure_desc=tire_pressure_desc,
        poor_tread_depth=poor_tread_depth,
        tread_depth_desc=tread_depth_desc,
        tire_damage=tire_damage,
        tire_damage_desc=tire_damage_desc,
        missing_lug_nuts=missing_lug_nuts,
        lug_nuts_desc=lug_nuts_desc,
        exterior_damage=exterior_damage,
        exterior_damage_desc=exterior_damage_desc,
        interior_damage=interior_damage,
        interior_damag_desc=interior_damag_desc,
        excessive_wear=excessive_wear,
        excessive_wear_desc=excessive_wear_desc,
        starting_issues=starting_issues,
        starting_issues_desc=starting_issues_desc,
        unusual_noise=unusual_noise,
        unusual_noise_desc=unusual_noise_desc,
        excessive_smoke=excessive_smoke,
        excessive_smoke_desc=excessive_smoke_desc,
        rough_transmission=rough_transmission,
        rough_transmission_desc=rough_transmission_desc,
        registration_expired=registration_expired,
        no_insurance_card=no_insurance_card,
        horn_failure=horn_failure,
        horn_failure_desc=horn_failure_desc,
        backup_alarm_failure=backup_alarm_failure,
        backup_alarm_desc=backup_alarm_desc,
        seatbelt_failure=seatbelt_failure,
        seatbelt_desc=seatbelt_desc,
        fire_extinguisher_old_missing=fire_extinguisher_old_missing,
        fire_extinguisher_desc=fire_extinguisher_desc,
        missing_safety_gear=missing_safety_gear,
        missing_safety_gear_desc=missing_safety_gear_desc,
        vehicle_id=vehicle_id,
        workorder_id=workorder_id,
    )
    session.add(inspection)
    session.flush()

    return inspection
