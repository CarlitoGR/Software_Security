from fastapi import APIRouter

router = APIRouter(prefix="/clinician", tags=["clinician"])

@router.get("/dashboard")
def clinician_dashboard() -> dict[str, str]:
    # TODO(team-clinician):
    # - Restrict to clinician/admin roles
    # - Return assigned patients or recent admissions
    return {"message": "Clinician dashboard placeholder"}
