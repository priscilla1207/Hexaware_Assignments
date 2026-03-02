# Enterprise Leave Management System (ELMS)

## Overview
A backend system for managing employee leave requests with role-based access control.

## Features
- Role-based access control (Admin, Manager, Employee)
- Leave application and approval workflow
- Department management
- Leave overlap validation
- Pagination and filtering

## Setup
```bash
cd day4_elms
pip install -r requirements.txt
python seed_data.py
uvicorn app.main:app --reload
```

## API Documentation
Visit: http://localhost:8000/docs

## Default Users
- Admin: admin@company.com / admin123
- Manager: manager@company.com / manager123
- Employee: employee@company.com / employee123

## Workflow
1. Employee applies for leave
2. Manager approves/rejects leave
3. Admin can override any decision
