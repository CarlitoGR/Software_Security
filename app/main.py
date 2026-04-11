from fastapi import FastAPI
from app.routes import auth, patients, admissions, clinician, audit

app = FastAPI(title="Patient Portal Team Scaffold")

app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(admissions.router)
app.include_router(clinician.router)
app.include_router(audit.router)

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Patient Portal Team Scaffold is running"}
