from os import getenv

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    app_name: str = getenv("APP_NAME", "Patient Portal")
    app_env: str = getenv("APP_ENV", "development")
    secret_key: str = getenv("SECRET_KEY", "change_me")

    database_url: str = getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/patient_portal",
    )


settings = Settings()
