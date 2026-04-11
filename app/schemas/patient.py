from pydantic import BaseModel

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str | None = None
    medical_record_number: str | None = None

    # TODO(team-records):
    # - Add stricter field validation
    # - Decide which fields are required
