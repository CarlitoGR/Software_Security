from sqlalchemy.orm import Session

from app.models.audit_log import AuditLog
from app.models.user import User


def write_audit_log(
    db: Session,
    user: User,
    action: str,
    resource: str,
    resource_id: str | None = None,
) -> None:
    audit_log = AuditLog(
        username=user.username,
        action=action,
        resource=resource,
        resource_id=resource_id,
    )

    db.add(audit_log)
    db.commit()
