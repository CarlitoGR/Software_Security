from sqlalchemy import Boolean, Column, Integer, String
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="patient")
    is_active = Column(Boolean, default=True)

    # TODO(team-auth):
    # - Add better role constraints
    # - Add account lockout / status fields if desired
    # - Decide whether patients are also users or linked separately
