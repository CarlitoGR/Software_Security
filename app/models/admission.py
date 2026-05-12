from sqlalchemy import Column, ForeignKey, Integer, String

from app.db import Base


class Admission(Base):
    __tablename__ = "admissions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    reason = Column(String, nullable=False)
    status = Column(String, nullable=False, default="admitted")
    admitted_at = Column(String, nullable=False)

    # TODO(team-admissions):
    # - Add timestamps
    # - Link to clinician or department
    # - Add foreign key relationships
