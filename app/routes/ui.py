from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Request, Query

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
    username = request.cookies.get("session_user")

    if not username:
        return RedirectResponse(url="/login", status_code=303)

    return templates.TemplateResponse(
        name="dashboard.html",
        context={"request": request, "username": username},
        request=request,
    )

@router.get("/patient-search")
def patient_search_page(request: Request, q: str = Query(default="")):
    username = request.cookies.get("session_user")

    if not username:
        return RedirectResponse(url="/login", status_code=303)

    return templates.TemplateResponse(
        name="patient_search.html",
        context={
            "request": request,
            "username": username,
            "query": q,
        },
        request=request,
    )
