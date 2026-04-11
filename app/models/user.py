from sqlalchemy import Column, Integer, String
from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

    # TODO(team-auth):
    # - Add better role constraints
    # - Add account lockout / status fields if desired
    # - Decide whether patients are also users or linked separately
