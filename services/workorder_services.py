from datetime import datetime, date
from models.WorkOrder import WorkOrder
from models.Database import engine
from models.enums.SeverityEnum import SeverityEnum
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic_schemas.WorkorderSchema import ReadWorkorder
from .vehicle_services import check_vehicle_exists


def create_workorder(
    name: str,
    severity: SeverityEnum,
    description: str,
    photo_path: str,
    vehicle_id: int,
    resolved_date: datetime | None = None,
    due_date: date | None = None,
) -> ReadWorkorder | None:
    with Session(engine) as session:
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
            session.commit()
            print("New work order created.")

            read_workorder = convert_to_readworkorder(workorder)
            return read_workorder

        print(f"Vehicle with primary key {vehicle_id} could not be found.")
        return None


def get_workorder(id: int) -> WorkOrder | None:
    with Session(engine) as s:
        stmt = select(WorkOrder).where(WorkOrder.primary_key == id)
        workorder = s.execute(stmt).scalars().first()

    return workorder


def get_workorders() -> list[WorkOrder] | None:
    with Session(engine) as s:
        stmt = select(WorkOrder)
        workorders: list[WorkOrder] = list(s.execute(stmt).scalars().all())

    return workorders


def convert_to_readworkorder(workorder: WorkOrder) -> ReadWorkorder:
    return ReadWorkorder.model_validate(workorder)


def convert_to_readworkorder_list(workorders: list[WorkOrder]) -> list[ReadWorkorder]:
    readworkorders: list[ReadWorkorder] = []
    for workorder in workorders:
        read_workorder = convert_to_readworkorder(workorder)
        readworkorders.append(read_workorder)

    return readworkorders
