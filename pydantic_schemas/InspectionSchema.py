from datetime import datetime
from pydantic import BaseModel, ConfigDict
from models.enums.QuestionTypesEnum import QuestionTypesEnum


class ReadInspectionItem(BaseModel):
    primary_key: int
    is_passed: bool | None
    description: str | None
    question_id: int
    inspection_id: int

    model_config = ConfigDict(from_attributes=True)


class ReadInspection(BaseModel):
    primary_key: int
    vehicle_id: int
    inspection_items: list[ReadInspectionItem]
    created_date: datetime

    model_config = ConfigDict(from_attributes=True)


class ReadInspectionQusestion(BaseModel):
    primary_key: int
    question: str
    is_active: bool
    question_type: QuestionTypesEnum
    inspection_items: list[ReadInspectionItem]

    model_config = ConfigDict(from_attributes=True)
