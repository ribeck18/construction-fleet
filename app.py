from fastapi import FastAPI

from routes.vehicle_routes import route as v_route
from routes.workorder_routes import route as w_route
from routes.html_routes import route as h_route


app = FastAPI()

app.include_router(v_route)
app.include_router(w_route)
app.include_router(h_route)
