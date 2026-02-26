# Learning Management System - Course Enrollment Platform

## Overview
Backend system for managing courses, students, and enrollments using FastAPI and Clean Architecture.

## Setup
```bash
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## API Documentation
Access Swagger UI at: http://localhost:8000/docs

## Architecture
- Controllers: API endpoints
- Services: Business logic
- Repositories: Data access
- Models: Database entities
- Schemas: Request/response validation
