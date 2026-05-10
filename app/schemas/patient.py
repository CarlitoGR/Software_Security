from pydantic import BaseModel

class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str | None = None
    gender: str
    phone: str | None = None


class PatientRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: str
    gender: str
    phone: str | None = None

    class Config:
        from_attributes = True


    # TODO(team-records):
    # - Add stricter field validation
    # - Decide which fields are required
