# Enterprise Asset Management System (EAMS)

## Overview
A centralized backend API system for managing physical and digital assets including laptops, mobile devices, monitors, software licenses, and company vehicles.

## Features
- Role-based access control (SuperAdmin, IT Admin, Manager, Employee)
- Asset lifecycle management
- Asset assignment tracking
- Asset request workflow
- Audit trail
- Pagination and filtering

## Setup
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Default Users
- SuperAdmin: superadmin@company.com / admin123
- IT Admin: itadmin@company.com / admin123
- Manager: manager@company.com / manager123
- Employee: employee@company.com / employee123
