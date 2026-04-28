from fastapi import APIRouter, HTTPException
from datetime import date, datetime
from pydantic_schemas.WorkorderSchema import ReadWorkorder
from models.WorkOrder import WorkOrder
from models.enums.SeverityEnum import SeverityEnum
from services.workorder_services import create_workorder, get_workorder, get_workorders

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
    workorder: ReadWorkorder | None = create_workorder(
        name,
        severity,
        description,
        photo_path,
        vehicle_id,
        resolved_date,
        due_date,
    )
    if workorder is None:
        raise HTTPException(
            status_code=404, detail=f"Vehicle with id {vehicle_id} could not be found."
        )

    return workorder


@route.get("/workorder{id}", response_model=ReadWorkorder)
async def retrieve_single_workorder(id: int):
    workorder: WorkOrder | None = get_workorder(id)
    if workorder is None:
        raise HTTPException(status_code=404, detail="Workorder not found")

    return workorder


@route.get("workorders", response_model=list[ReadWorkorder])
async def retrieve_workorder_list():
    workorders: list[WorkOrder] | None = get_workorders()
    if workorders is None:
        raise HTTPException(status_code=404, detail="No workorders found.")
