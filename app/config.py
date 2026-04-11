from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "Patient Portal")
    app_env: str = os.getenv("APP_ENV", "development")
    secret_key: str = os.getenv("SECRET_KEY", "change_me")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./patient_portal.db")

settings = Settings()
