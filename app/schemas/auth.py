from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

    # TODO(team-auth):
    # - Add stronger validation rules if needed
