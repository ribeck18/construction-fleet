from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from services.vehicle_services import get_vehicles, get_counts_dict
from services.workorder_services import get_workorders


route = APIRouter()
templates = Jinja2Templates(directory="templates")


@route.get("/", response_class=HTMLResponse)
async def get_home_page(request: Request):
    vehicles = get_vehicles()
    workorders = get_workorders()
    counts_dict = get_counts_dict()
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
