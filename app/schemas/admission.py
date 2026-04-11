from pydantic import BaseModel

class AdmissionCreate(BaseModel):
    patient_id: int
    reason: str | None = None

    # TODO(team-admissions):
    # - Add validation rules
    # - Decide required intake fields
