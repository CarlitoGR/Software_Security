# 🏥 Patient Portal System (Team Project)

## 📌 Overview

This project is a **secure patient portal web application** built with **Python (FastAPI)** and a relational database.

The system is designed to simulate a healthcare environment where patient data must be handled with **privacy, security, and controlled access** in mind (HIPAA-inspired principles).

This repository contains a **team scaffold**, providing structure and direction while leaving core features to be implemented collaboratively.

---

## 🎯 Objectives

The system aims to support:

* Secure patient login
* Patient record storage and retrieval
* Patient search functionality
* Viewing patient information
* Patient admission workflows
* Clinician-specific views
* Audit logging of sensitive data access
* Security-focused design and threat modeling

---

## 🧱 Project Structure

```text
app/
├── main.py            # Application entry point
├── config.py          # Environment/config management
├── db.py              # Database setup
├── models/            # Database models
├── routes/            # API endpoints
├── schemas/           # Request/response validation
├── services/          # Business logic layer
└── security/          # Security utilities

docs/
├── team_tasks.md      # Suggested team breakdown
└── threat_model.md    # Security analysis starter

tests/                 # Placeholder for tests
```

---

## ⚙️ Tech Stack

* **Backend:** FastAPI
* **Database:** SQLite (starter) → PostgreSQL (recommended)
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Security:** Passlib (planned), role-based access (planned)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd patient-portal
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
copy .env.example .env
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

### 6. Open in browser

* API: http://127.0.0.1:8000
* Login: http://127.0.0.1:8000/login  (Placeholder non-functioning)
* Docs: http://127.0.0.1:8000/docs

---

## 👥 Team Responsibilities

This project is intentionally incomplete to allow **equal contribution**.

Suggested areas of ownership:

| Area             | Responsibilities                               |
| ---------------- | ---------------------------------------------- |
| Authentication   | Login, password hashing, sessions/JWT, roles   |
| Patient Records  | CRUD operations, validation, data structure    |
| Search           | Filtering, secure queries, access restrictions |
| Admissions       | Admission workflow, status tracking            |
| Clinician View   | Role-restricted endpoints, dashboards          |
| Audit & Security | Logging, threat modeling, access tracking      |

See: `docs/team_tasks.md`

---

## 🔐 Security Focus

This system is designed with **security-first thinking**:

### Key Concerns

* Protecting sensitive health information (PHI)
* Preventing unauthorized access
* Securing user input and database queries
* Tracking access to patient data

### Planned Controls

* Password hashing (bcrypt/passlib)
* Role-based access control (RBAC)
* Audit logging for sensitive operations
* Input validation and sanitization
* Least-privilege access design

---

## ⚠️ Disclaimer

This project is **for educational purposes only**.

It is **NOT HIPAA-compliant** and should not be used in a real healthcare environment without significant additional security, compliance, and legal validation.

---

## 🧠 Threat Modeling

Initial threat considerations include:

* Unauthorized data access
* Injection attacks
* Credential compromise
* Data leakage through logs
* Insider misuse

See: `docs/threat_model.md`

---

## 🛠️ Future Enhancements

* JWT-based authentication
* PostgreSQL + migrations
* Encryption for sensitive fields
* Rate limiting and brute-force protection
* Full audit trail with timestamps and IP tracking
* Dockerized deployment
* Frontend UI integration

---

## 🤝 Contribution Guidelines

* Pick a feature area and create a branch
* Follow existing project structure
* Add comments and TODOs where needed
* Test your endpoints before merging
* Participate in security review discussions

---

## 📄 License

This project is for academic use. Add a license if required by your course.
