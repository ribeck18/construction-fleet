from pydantic import BaseModel, ConfigDict
from datetime import datetime, date
from models.enums.SeverityEnum import SeverityEnum


class ReadWorkorder(BaseModel):
    primary_key: int
    name: str
    severity: SeverityEnum
    description: str
    photo_path: str
    vehicle_id: int
    created_date: datetime
    resolved_date: datetime | None
    due_date: date | None

    model_config = ConfigDict(from_attributes=True)
