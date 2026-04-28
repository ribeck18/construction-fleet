from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

_ = load_dotenv()

conn_string: str = os.environ["CONNECTION_STRING"]

engine = create_engine(conn_string)


class Base(DeclarativeBase):
    pass


def create_tables() -> None:
    print("Tables known to Base.metadata:", list(Base.metadata.tables.keys()))
    Base.metadata.create_all(engine)
