from dotenv import load_dotenv

_ = load_dotenv()
import os

print(f"FILE_PATH = {repr(os.environ.get('FILE_PATH', '<MISSING>'))}")
print(
    f"CONNECTION_STRING = {repr(os.environ.get('CONNECTION_STRING', '<MISSING>')[:20])}..."
)
import models  # This imports all the models in the models directory so that tables are written at runtime.
import uvicorn
from models.Database import create_tables

if __name__ == "__main__":
    create_tables()

    uvicorn.run("app:app", reload=True)
