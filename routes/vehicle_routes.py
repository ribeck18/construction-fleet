from fastapi import APIRouter, HTTPException
from models.Vehicle import Vehicle
from models.Database import engine
from pydantic_schemas.VehicleSchema import ReadVehicle
from services.vehicle_services import (
    create_vehicle,
    get_vehicles,
    get_vehicle,
    convert_to_read_vehicle,
)
from sqlalchemy.orm import Session

route = APIRouter()


@route.post("/create-vehicle")
async def new_vehicle(
    name: str, make: str, model: str, year: int, vin: str
) -> ReadVehicle:
    with Session(engine) as session:
        vehicle = create_vehicle(session, name, make, model, year, vin)
        read_vehicle = convert_to_read_vehicle(vehicle)
        session.commit()

    return read_vehicle


@route.get("/vehicles", response_model=list[ReadVehicle])
async def retrieve_vehicles() -> list[Vehicle]:
    with Session(engine) as session:
        vehicles: list[Vehicle] = get_vehicles(session)
    return vehicles


@route.get("/vehicle{id}", response_model=ReadVehicle)
async def retrive_vehicle(id: int) -> Vehicle:
    with Session(engine) as session:
        vehicle: Vehicle | None = get_vehicle(session, id)
        if vehicle is None:
            raise HTTPException(status_code=404, detail="Vehicle not found")

    return vehicle
