# Patient Portal Team Scaffold

This project is a **team-ready scaffold** for a secure patient portal built with **FastAPI + SQLAlchemy**.

It intentionally includes:
- Working app startup
- Folder structure
- Placeholder routers
- Placeholder models
- Clear TODO markers
- Team ownership suggestions

It intentionally does **not** include a fully completed system, so each teammate can meaningfully contribute.

## Features to Build
- Secure patient login
- Store patient records
- Search for patients
- View patient information
- Process patient admissions
- Simple clinician view
- Audit logs for health data access
- Privacy and confidentiality controls
- Secure input handling
- Threat modeling for unauthorized access and data leakage

## Suggested Team Split
1. **Authentication & Access Control**
   - Login flow
   - Password hashing
   - Role-based access
   - Session or token strategy

2. **Patient Records**
   - Patient model
   - Create/read/update logic
   - Data validation

3. **Patient Search**
   - Search routes
   - Filtering logic
   - Result restrictions based on role

4. **Admissions**
   - Admission model
   - Intake workflow
   - Status tracking

5. **Clinician View**
   - Clinician-specific endpoints
   - Assigned-patient view
   - Access boundaries

6. **Audit & Security Review**
   - Audit logging
   - Sensitive access tracking
   - Threat model writeup
   - Security test checklist

## Quick Start
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Open:
- API root: `http://127.0.0.1:8000/`
- Docs: `http://127.0.0.1:8000/docs`

## Notes
- This scaffold is **HIPAA-inspired**, not HIPAA certified.
- SQLite is included for easy startup. You can later switch to PostgreSQL.
- The database tables are not fully modeled yet on purpose.

## Team Planning Prompt
Before building, decide:
- SQL vs MongoDB final choice
- JWT vs server-side sessions
- Which fields count as sensitive PHI
- Which actions must always be audit logged
- Which roles can search or view patient records
