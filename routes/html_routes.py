from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from models.Database import engine
from services.vehicle_services import get_vehicles, get_counts_dict
from services.workorder_services import get_workorders


route = APIRouter()
templates = Jinja2Templates(directory="templates")


@route.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    with Session(engine) as session:
        vehicles = get_vehicles(session)
        workorders = get_workorders(session)
        counts_dict = get_counts_dict(session)

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "page_title": "Dashboard",
            "vehicles": vehicles,
            "workorders": workorders,
            "user": "John Doe",
            "counts": counts_dict,
        },
    )
