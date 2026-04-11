from sqlalchemy import Column, Integer, String
from app.db import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    actor_username = Column(String, nullable=False)
    action = Column(String, nullable=False)
    target_type = Column(String, nullable=False)
    target_id = Column(String, nullable=True)

    # TODO(team-audit):
    # - Add timestamp
    # - Add IP address or request source if desired
    # - Decide which reads and writes must always be logged
