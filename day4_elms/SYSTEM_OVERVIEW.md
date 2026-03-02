# Enterprise Leave Management System - Overview

## Architecture

### Clean Architecture Layers

1. **Controllers** - Handle HTTP requests and responses
2. **Services** - Business logic and validation
3. **Repositories** - Database operations
4. **Models** - SQLAlchemy ORM entities
5. **Schemas** - Pydantic validation

## Key Features

✅ JWT Authentication
✅ Role-Based Access Control (RBAC)
✅ Leave overlap validation
✅ Date validation (no past dates)
✅ Department-based leave management
✅ Pagination for large datasets
✅ Middleware logging
✅ Global exception handling
✅ Clean layered architecture

## User Roles & Permissions

### Admin
- Create users
- Create departments
- View all leaves (company-wide)
- Override any leave decision

### Manager
- View department employees
- View department leaves
- Approve/reject department leaves

### Employee
- Apply for leave
- View own leave history

## Database Schema

### User
- id, name, email, password, role, department_id

### Department
- id, name, manager_id

### LeaveRequest
- id, employee_id, start_date, end_date, reason, status, approved_by

## Workflow

1. Employee applies for leave → Status: PENDING
2. Manager reviews and approves/rejects
3. Admin can override any decision

## Validation Rules

- Start date must be before end date
- Cannot apply for past dates
- No overlapping leave requests
- Manager can only approve leaves from their department
- Leave must be PENDING to be processed
