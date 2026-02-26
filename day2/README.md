# Loan Application & Approval Management System

## Overview
Backend API system for digitizing loan processing workflow with automated eligibility validation and status tracking.

## Business Rules
- Maximum eligible loan = income × 10
- Only PENDING loans can be approved or rejected
- Loans exceeding eligibility are automatically rejected

## Features
- Submit loan applications
- Automatic eligibility validation
- Approve/reject loans
- Track application status
- Business rule enforcement

## Setup
```bash
cd day2
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## API Documentation
Access Swagger UI at: http://localhost:8000/docs

## Architecture
Clean Architecture with layered separation:
- Controllers: API endpoints
- Services: Business logic & validation
- Repositories: Data access
- Models: Database entities
- Schemas: Request/response validation

## API Endpoints

### Submit Loan Application
```
POST /loans
Body: {
  "applicant_name": "Rahul Kumar",
  "income": 50000,
  "loan_amount": 200000
}
```

### Get Loan by ID
```
GET /loans/{loan_id}
```

### Get All Loans
```
GET /loans
```

### Approve Loan
```
PUT /loans/{loan_id}/approve
```

### Reject Loan
```
PUT /loans/{loan_id}/reject
```

## Status Codes
- 201: Loan created
- 200: Success
- 400: Business validation failed
- 404: Not found
- 422: Invalid input
