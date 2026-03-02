# Quick Start Guide - EAMS

## Installation

```bash
cd day3_eams
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
| SuperAdmin | superadmin@company.com | admin123 |
| IT Admin | itadmin@company.com | admin123 |
| Manager | manager@company.com | manager123 |
| Employee | employee@company.com | employee123 |

## API Endpoints

### Authentication
- POST /auth/login

### SuperAdmin
- POST /superadmin/assets
- POST /superadmin/users
- POST /superadmin/departments

### IT Admin
- POST /itadmin/assets
- GET /itadmin/assets?status=AVAILABLE&page=1&size=20
- POST /itadmin/assignments

### Manager
- GET /manager/department-assets

### Employee
- POST /employee/requests
- GET /employee/my-assets

## Example Workflow

1. Login as IT Admin
2. Create an asset
3. Login as Employee
4. Request an asset
5. Login as IT Admin
6. Approve request and assign asset
