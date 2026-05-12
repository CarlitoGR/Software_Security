from pydantic import BaseModel


class AdmissionCreate(BaseModel):
    patient_id: int
    reason: str
    admitted_at: str
    status: str = "admitted"


class AdmissionRead(BaseModel):
    id: int
    patient_id: int
    reason: str
    admitted_at: str
    status: str

    class Config:
        from_attributes = True
    
    # TODO(team-admissions):
    # - Add validation rules
    # - Decide required intake fields
