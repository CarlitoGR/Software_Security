from time import sleep

from fastapi import FastAPI
from sqlalchemy.exc import OperationalError

from app.routes import auth, patients, admissions, clinician, audit
from app.db import Base, engine

app = FastAPI(title="Patient Portal Team Scaffold")


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
app.include_router(clinician.router)
app.include_router(audit.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Patient Portal Team Scaffold is running"}
