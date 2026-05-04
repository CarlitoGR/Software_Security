from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "password":
        return RedirectResponse(url="/dashboard", status_code=303)

    return HTMLResponse(
        """
        <h1>Login Failed</h1>
        <p>Invalid username or password.</p>
        <a href="/login">Try again</a>
        """,
        status_code=401,
    )
