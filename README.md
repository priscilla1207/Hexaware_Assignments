# FastAPI Learning Projects

This repository contains my FastAPI learning assignments with Clean Architecture implementation.

## Day 1 - Learning Management System (LMS)
Course enrollment platform with student, course, and enrollment management.

**Features:**
- Student registration
- Course management
- Enrollment system with duplicate prevention
- REST APIs with Swagger documentation

**Run Day 1:**
```bash
cd day1-lms
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs

---

## Day 2 - Loan Application & Approval Management System
Fintech loan processing workflow with automated eligibility validation.

**Features:**
- Submit loan applications
- Automatic eligibility validation (max loan = income × 10)
- Approve/reject loans with business rule enforcement
- Status tracking and audit trail
- Only PENDING loans can be approved/rejected

**Run Day 2:**
```bash
cd day2
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000/docs

---

## Architecture
Both projects follow Clean Architecture principles:
- **Controllers**: API endpoints (HTTP layer)
- **Services**: Business logic & validation
- **Repositories**: Data access layer
- **Models**: Database entities (SQLAlchemy ORM)
- **Schemas**: Request/response validation (Pydantic)
- **Dependencies**: Dependency injection

## Structure
```
.
├── day1-lms/          # LMS Course Enrollment Platform
├── day2/              # Loan Application Management System
└── README.md          # This file
```

## Tech Stack
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Uvicorn
