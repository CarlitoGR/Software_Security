from sqlalchemy import Column, Integer, String
from app.db import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=True)
    gender = Column(String, nullable=False)
    phone = Column(String, nullable=True)

    # TODO(team-records):
    # - Add contact info, emergency contact, diagnoses, or insurance fields as needed
    # - Decide which fields count as highly sensitive PHI
    # - Add encryption strategy discussion for sensitive fields
