from time import sleep

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from app.routes import auth, patients, admissions, audit, ui
from app.db import Base, engine

app = FastAPI(
    title="Secure Patient Portal API",
    version="1.0.0",
    description=(
        "A secure healthcare-style backend API using FastAPI, "
        "JWT authentication, PostgreSQL, Docker, and Alembic.\n\n"
        "Current MVP features include authentication and patient management.\n\n"
        "Additional modules such as admissions, clinician workflows, "
        "audit logging, and UI integration are planned for future implementation."
    ),
)


@app.on_event("startup")
def startup() -> None:
    for attempt in range(15):
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connection established.")
            return
        except OperationalError as exc:
            print(f"Database not ready yet. Attempt {attempt + 1}/15")
            print(exc)
            sleep(2)

    raise RuntimeError("Database was not ready after multiple attempts.")


app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(admissions.router)
app.include_router(audit.router)
app.include_router(ui.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Patient Portal Team Scaffold is running"}
