from fastapi import APIRouter, HTTPException
from datetime import date, datetime
from sqlalchemy.orm import Session
from pydantic_schemas.InspectionSchema import ReadInspection
from models.WorkOrder import WorkOrder
from models.Database import engine
from models.Vehicle import Vehicle
from models.Inspection import Inspection
from services.inspection_services import convert_to_readinspection, create_inspection

route = APIRouter()


@route.post("/create-inspection")
def new_inspection(
    question_id: int,
    inspection_id: int,
    is_passed: bool | None = None,
    description: str | None = None,
) -> ReadInspection:
    with Session(engine) as s:
        inspection: Inspection = Inspection(
            session=s,
            question_id=question_id,
            inspection_id=inspection_id,
            is_passed=is_passed,
            description=description,
        )
        readinspection = convert_to_readinspection(inspection)
        s.commit()

        return readinspection


@route.post("/create-question")
def new_question():
    pass
