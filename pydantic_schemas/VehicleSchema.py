from pydantic import BaseModel, ConfigDict
from models.enums.StatusEnum import Status


class CreateVehicle(BaseModel):
    name: str
    make: str
    model: str
    year: int
    vin: str | None


class ReadVehicle(BaseModel):
    primary_key: int
    vin: str
    name: str
    make: str
    model: str
    year: int
    status: Status

    model_config = ConfigDict(from_attributes=True)
