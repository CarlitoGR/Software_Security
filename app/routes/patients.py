from fastapi import APIRouter

router = APIRouter(prefix="/patients", tags=["patients"])

@router.get("/")
def list_patients() -> dict[str, str]:
    # TODO(team-records/search):
    # - Restrict access by role
    # - Return filtered patient list
    return {"message": "List patients placeholder"}

@router.get("/search")
def search_patients() -> dict[str, str]:
    # TODO(team-search):
    # - Add query parameters
    # - Search by name, MRN, DOB, or other allowed fields
    # - Prevent overbroad results and unauthorized lookup
    return {"message": "Search patients placeholder"}

@router.get("/{patient_id}")
def get_patient(patient_id: int) -> dict[str, str | int]:
    # TODO(team-records/audit):
    # - Validate caller permissions
    # - Load patient record
    # - Audit this access
    return {"message": "Get patient placeholder", "patient_id": patient_id}
