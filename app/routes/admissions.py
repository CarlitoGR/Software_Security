from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.admission import Admission
from app.models.patient import Patient
from app.models.user import User
from app.schemas.admission import AdmissionCreate, AdmissionRead
from app.security import get_current_user
from app.services.audit import write_audit_log

router = APIRouter(prefix="/admissions", tags=["Admissions"])


@router.post(
    "/",
    response_model=AdmissionRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create an admission record",
)
def create_admission(
    admission_data: AdmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Admission:
    patient = db.query(Patient).filter(Patient.id == admission_data.patient_id).first()

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found.",
        )

    admission = Admission(
        patient_id=admission_data.patient_id,
        reason=admission_data.reason,
        admitted_at=admission_data.admitted_at,
        status=admission_data.status,
    )

    db.add(admission)
    db.commit()
    db.refresh(admission)

    write_audit_log(
        db=db,
        user=current_user,
        action="create_admission",
        resource="admission",
        resource_id=str(admission.id),
    )

    return admission


@router.get(
    "/",
    response_model=list[AdmissionRead],
    summary="List admission records",
)
def list_admissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[Admission]:
    write_audit_log(
        db=db,
        user=current_user,
        action="list_admissions",
        resource="admission",
    )

    return db.query(Admission).all()


@router.get(
    "/{admission_id}",
    response_model=AdmissionRead,
    summary="Get an admission record by ID",
)
def get_admission(
    admission_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Admission:
    admission = db.query(Admission).filter(Admission.id == admission_id).first()

    if admission is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Admission not found.",
        )

    write_audit_log(
        db=db,
        user=current_user,
        action="get_admission",
        resource="admission",
        resource_id=str(admission.id),
    )

    return admission
