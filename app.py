from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.vehicle_routes import route as v_route
from routes.workorder_routes import route as w_route
from routes.html_routes import route as h_route
from routes.inspection_routes import route as i_route


app = FastAPI()

app.include_router(v_route)
app.include_router(w_route)
app.include_router(h_route)
app.include_router(i_route)
app.mount("/static", StaticFiles(directory="static"), name="static")
