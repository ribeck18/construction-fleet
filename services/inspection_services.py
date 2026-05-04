from datetime import datetime
from models.Inspection import Inspection, InspectionItem, InspectionQuestion
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


def get_issues():
    pass


def initiate_new_workorder():
    pass


def create_inspection_item(
    session: Session,
    question_id: int,
    inspection_id: int,
    is_passed: bool | None = None,
    description: str | None = None,
) -> InspectionItem:
    item = InspectionItem(
        question_id=question_id,
        inspection_id=inspection_id,
        is_passed=is_passed,
        description=description,
    )

    session.add(item)
    session.flush()

    return item


def create_inspection(session: Session, vehicle_id: int) -> Inspection:
    inspection: Inspection = Inspection(vehicle_id=vehicle_id)
    questions = get_active_questions(session)

    for question in questions:
        inspection_item = create_inspection_item(
            session, question.primary_key, inspection.primary_key
        )

        inspection.inspection_items.append(inspection_item)

    session.add(inspection)
    session.flush()

    return inspection


def get_active_questions(session: Session) -> list[InspectionQuestion]:
    stmt = select(InspectionQuestion).where(InspectionQuestion.is_active)
    questions = list(session.execute(stmt).scalars().all())

    return questions
