from fastapi import APIRouter, HTTPException
from models.Vehicle import Vehicle
from pydantic_schemas.VehicleSchema import ReadVehicle
from services.vehicle_services import create_vehicle, get_vehicles, get_vehicle

route = APIRouter()


@route.post("/create-vehicle")
async def new_vehicle(
    name: str, make: str, model: str, year: int, vin: str
) -> ReadVehicle:
    vehicle = create_vehicle(name, make, model, year, vin)

    return vehicle


@route.get("/vehicles", response_model=list[ReadVehicle])
async def retrieve_vehicles() -> list[Vehicle]:
    vehicles: list[Vehicle] = get_vehicles()
    return vehicles


@route.get("/vehicle{id}", response_model=ReadVehicle)
async def retrive_vehicle(id: int) -> Vehicle:
    vehicle: Vehicle | None = get_vehicle(id)
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return vehicle
