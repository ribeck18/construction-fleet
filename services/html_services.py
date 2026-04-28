from models.Database import engine
from sqlalchemy.orm import Session
from .vehicle_services import get_counts_dict, get_vehicles_with_issue


def get_dash_data() -> dict[str, dict]:
    with Session(engine) as session:
        vehicles_with_issue = get_vehicles_with_issue(session)
