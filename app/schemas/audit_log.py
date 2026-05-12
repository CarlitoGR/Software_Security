from datetime import datetime

from pydantic import BaseModel


class AuditLogRead(BaseModel):
    id: int
    username: str
    action: str
    resource: str
    resource_id: str | None
    created_at: datetime

    class Config:
        from_attributes = True
