from fastapi import APIRouter, HTTPException
from datetime import date, datetime
from sqlalchemy.orm import Session
from pydantic_schemas.WorkorderSchema import ReadWorkorder
from models.WorkOrder import WorkOrder
from models.Database import engine
from models.enums.SeverityEnum import SeverityEnum
from services.workorder_services import (
    create_workorder,
    get_workorder,
    get_workorders,
    convert_to_readworkorder,
)

route = APIRouter()


@route.post("/create-workorder")
async def new_workorder(
    name: str,
    severity: SeverityEnum,
    description: str,
    photo_path: str,
    vehicle_id: int,
    resolved_date: datetime | None = None,
    due_date: date | None = None,
) -> ReadWorkorder:
    with Session(engine) as session:
        workorder: WorkOrder | None = create_workorder(
            session,
            name,
            severity,
            description,
            photo_path,
            vehicle_id,
            resolved_date,
            due_date,
        )
        read_workorder = convert_to_readworkorder(workorder)
        session.commit()

    return read_workorder


@route.get("/workorder{id}", response_model=ReadWorkorder)
async def retrieve_single_workorder(id: int):
    with Session(engine) as session:
        workorder: WorkOrder | None = get_workorder(session, id)
        if workorder is None:
            raise HTTPException(status_code=404, detail="Workorder not found")

    return workorder


@route.get("/workorders", response_model=list[ReadWorkorder])
async def retrieve_workorder_list():
    with Session(engine) as session:
        workorders: list[WorkOrder] | None = get_workorders(session)
        if workorders is None:
            raise HTTPException(status_code=404, detail="No workorders found.")

    return workorders
