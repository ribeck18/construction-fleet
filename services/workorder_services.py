from datetime import datetime, date
from models.WorkOrder import WorkOrder
from models.enums.SeverityEnum import SeverityEnum
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic_schemas.WorkorderSchema import ReadWorkorder
from .vehicle_services import check_vehicle_exists


def create_workorder(
    session: Session,
    name: str,
    severity: SeverityEnum,
    description: str,
    photo_path: str,
    vehicle_id: int,
    resolved_date: datetime | None = None,
    due_date: date | None = None,
) -> WorkOrder | None:
    vehicle_exists = check_vehicle_exists(session=session, id=vehicle_id)
    if vehicle_exists:
        workorder = WorkOrder(
            name=name,
            severity=severity,
            description=description,
            photo_path=photo_path,
            vehicle_id=vehicle_id,
            resolved_date=resolved_date,
            due_date=due_date,
        )
        session.add(workorder)
        session.flush()

        return workorder

    else:
        return None


def get_workorder(session: Session, id: int) -> WorkOrder | None:
    stmt = select(WorkOrder).where(WorkOrder.primary_key == id)
    workorder = session.execute(stmt).scalars().first()

    return workorder


def get_workorders(session: Session) -> list[WorkOrder] | None:
    stmt = select(WorkOrder)
    workorders: list[WorkOrder] = list(session.execute(stmt).scalars().all())

    return workorders


def convert_to_readworkorder(workorder: WorkOrder) -> ReadWorkorder:
    return ReadWorkorder.model_validate(workorder)


def convert_to_readworkorder_list(workorders: list[WorkOrder]) -> list[ReadWorkorder]:
    readworkorders: list[ReadWorkorder] = []
    for workorder in workorders:
        read_workorder = convert_to_readworkorder(workorder)
        readworkorders.append(read_workorder)

    return readworkorders
