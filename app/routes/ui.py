from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["ui"])

templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse(
        name="login.html",
        context={"request": request},
        request=request,
    )

@router.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse(
        name="dashboard.html",
        context={"request": request},
        request=request,
    )
