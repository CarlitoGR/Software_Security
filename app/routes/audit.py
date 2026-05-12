from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.audit_log import AuditLog
from app.models.user import User
from app.schemas.audit_log import AuditLogRead
from app.security import get_current_user

router = APIRouter(prefix="/audit", tags=["Audit"])


@router.get(
    "/",
    response_model=list[AuditLogRead],
    summary="List audit logs",
)
def list_audit_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[AuditLog]:
    return db.query(AuditLog).order_by(AuditLog.created_at.desc()).all()
