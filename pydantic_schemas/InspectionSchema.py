from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ReadInspection(BaseModel):
    # Basic Data
    primary_key: int
    name: str
    created_date: datetime
    current_mileage: int

    # Safety/critical data
    brakes_bad: bool
    brakes_desc: str | None
    park_brake_fail: bool
    park_brake_desc: str | None
    steering_issues: bool
    steering_desc: str | None
    lights_out: bool
    lights_desc: str | None
    signals_out: bool
    signals_desc: str | None
    mirrors_broken: bool
    mirrors_desc: str | None
    windshield_broken: bool
    windshield_desc: str | None

    # Mechanical
    oil_level_low: bool
    oil_level_desc: str | None
    coolant_level_low: bool
    coolant_level_desc: str | None
    leaks: bool
    leaks_desc: str | None
    trans_fluid_level_low: bool
    trans_fluid_level_desc: str | None
    bad_battery: bool
    battery_desc: str | None
    warning_lights: bool
    warning_desc: str | None
    poor_tire_pressure: bool
    tire_pressure_desc: str | None
    poor_tread_depth: bool
    tread_depth_desc: str | None
    tire_damage: bool
    tire_damage_desc: str | None
    missing_lug_nuts: bool
    lug_nuts_desc: str | None

    # Damage/wear
    exterior_damage: bool
    exterior_damage_desc: str | None
    interior_damage: bool
    interior_damag_desc: str | None
    excessive_wear: bool
    excessive_wear_desc: str | None

    # Operation Check
    starting_issues: bool
    starting_issues_desc: str | None
    unusual_noise: bool
    unusual_noise_desc: str | None
    excessive_smoke: bool
    excessive_smoke_desc: str | None
    rough_transmission: bool
    rough_transmission_desc: str | None

    # Documents
    registration_expired: bool
    no_insurance_card: bool

    # Safety Equipment
    horn_failure: bool
    horn_failure_desc: str | None
    backup_alarm_failure: bool
    backup_alarm_desc: str | None
    seatbelt_failure: bool
    seatbelt_desc: str
    fire_extinguisher_old_missing: bool
    fire_extinguisher_desc: str | None
    missing_safety_gear: bool
    missing_safety_gear_desc: str | None

    # Relationships
    vehicle_id: int
    workorder_id: int

    model_config = ConfigDict(from_attributes=True)
