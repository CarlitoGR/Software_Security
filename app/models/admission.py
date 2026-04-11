from sqlalchemy import Column, Integer, String
from app.db import Base

class Admission(Base):
    __tablename__ = "admissions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, nullable=False)
    status = Column(String, nullable=False, default="pending")
    reason = Column(String, nullable=True)

    # TODO(team-admissions):
    # - Add timestamps
    # - Link to clinician or department
    # - Add foreign key relationships
