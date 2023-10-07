from pydantic import validator
from pydantic_settings import BaseSettings


class SettingsDatabase(BaseSettings):
    @validator("LOCAL_URI", pre=True, check_fields=False)
    def __init__(self) -> None:
        self.connection_string = "mongodb://localhost:27017/"

database = SettingsDatabase()