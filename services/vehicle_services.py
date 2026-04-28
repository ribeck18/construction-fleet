from models.Vehicle import Vehicle
from models.enums import StatusEnum
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from pydantic_schemas.VehicleSchema import ReadVehicle


def create_vehicle(
    session: Session, name: str, make: str, model: str, year: int, vin: str
) -> Vehicle:
    vehicle: Vehicle = Vehicle(name=name, make=make, model=model, year=year, vin=vin)
    session.add(vehicle)
    session.flush()

    return vehicle


def get_vehicles(session: Session) -> list[Vehicle]:
    stmt = select(Vehicle)
    vehicles = list(session.execute(stmt).scalars().all())
    return vehicles


def get_vehicle(session: Session, id: int) -> Vehicle | None:
    stmt = select(Vehicle).where(Vehicle.primary_key == id)
    vehicle = session.execute(stmt).scalars().first()

    return vehicle


def get_vehicle_name(vehicle: Vehicle) -> str:
    name: str = f"{vehicle.year} {vehicle.make} {vehicle.model}: {vehicle.name}"

    return name


def convert_to_read_vehicle(vehicle: Vehicle) -> ReadVehicle:
    return ReadVehicle.model_validate(vehicle)


def convert_to_read_vehicle_list(vehicles: list[Vehicle]) -> list[ReadVehicle]:
    readvehicles: list[ReadVehicle] = []
    for vehicle in vehicles:
        v = convert_to_read_vehicle(vehicle)
        readvehicles.append(v)

    return readvehicles


def check_vehicle_exists(session: Session, id: int) -> bool:
    stmt = select(Vehicle).where(Vehicle.primary_key == id)
    vehicle: Vehicle | None = session.execute(stmt).scalars().first()

    if vehicle is None:
        return False
    else:
        return True


def get_counts_dict(session: Session) -> dict[str, int]:
    down = get_specific_count(session, StatusEnum.Status.DOWN)
    in_shop = get_specific_count(session, StatusEnum.Status.IN_SHOP)
    needs_attention = get_specific_count(session, StatusEnum.Status.NEEDS_ATTENTION)
    active = get_specific_count(session, StatusEnum.Status.ACTIVE)
    vehicles = get_count(session)

    counts_dict = {
        "down": down,
        "in_shop": in_shop,
        "needs_attention": needs_attention,
        "active": active,
        "vehicles": vehicles,
    }

    return counts_dict


def get_count(session: Session) -> int:
    stmt = select(func.count()).select_from(Vehicle)

    count = session.execute(stmt).scalar()
    if count is None:
        count = 0

    return count


def get_specific_count(session: Session, status: StatusEnum.Status | None) -> int:
    stmt = select(func.count()).select_from(Vehicle).where(Vehicle.status == status)

    count = session.execute(stmt).scalar()
    if count is None:
        count = 0

    return count


def get_vehicles_with_issue(session: Session) -> list[Vehicle]:
    stmt = select(Vehicle).where(Vehicle.status != StatusEnum.Status.ACTIVE)
    vehicles: list[Vehicle] = list(session.execute(stmt).scalars().all())

    return vehicles
