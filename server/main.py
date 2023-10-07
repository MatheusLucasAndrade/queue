import os
from fastapi import FastAPI

from app.api.api_router import api_router
from dotenv import load_dotenv

load_dotenv()

database_uri = os.getenv("LOCAL_URI")
database_name = os.getenv("DB_NAME")

app = FastAPI(title="Queue", openapi_url="/", root_path="")

app.include_router(api_router, prefix="/api")
