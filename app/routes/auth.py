from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login() -> dict[str, str]:
    # TODO(team-auth):
    # - Accept username + password
    # - Verify password hash
    # - Return token/session
    # - Log failed and successful login attempts
    return {"message": "Login placeholder"}
