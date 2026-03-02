# Quick Start Guide - ELMS

## Installation

```bash
cd day4_elms
pip install -r requirements.txt
```

## Initialize Database

```bash
python seed_data.py
```

## Run Application

```bash
uvicorn app.main:app --reload --port 8000
```

## API Documentation
Visit: http://localhost:8000/docs

## Test Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | admin@company.com | admin123 |
| Manager | manager@company.com | manager123 |
| Employee | employee@company.com | employee123 |

## API Endpoints

### Authentication
- POST /auth/login

### Admin
- POST /admin/users
- GET /admin/users
- POST /admin/departments
- GET /admin/departments
- GET /admin/leaves?status=PENDING&page=1&size=20
- PUT /admin/leaves/{leave_id}

### Manager
- GET /manager/leaves?status=PENDING&page=1&size=20
- PUT /manager/leaves/{leave_id}

### Employee
- POST /employee/leaves
- GET /employee/leaves

## Example Workflow

1. Login as Employee
2. Apply for leave
3. Login as Manager
4. Approve/reject leave
5. Login as Admin
6. View all leaves

## JSON Examples

### Login
```json
{
  "email": "employee@company.com",
  "password": "employee123"
}
```

### Apply Leave
```json
{
  "start_date": "2026-03-10",
  "end_date": "2026-03-12",
  "reason": "Personal work"
}
```

### Approve/Reject Leave
```json
{
  "status": "APPROVED"
}
```

### Create User (Admin)
```json
{
  "name": "New Employee",
  "email": "newemp@company.com",
  "role": "EMPLOYEE",
  "department_id": 1,
  "password": "password123"
}
```

### Create Department (Admin)
```json
{
  "name": "Marketing",
  "manager_id": 2
}
```
