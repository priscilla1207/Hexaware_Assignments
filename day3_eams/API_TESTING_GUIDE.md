# API Testing Guide

## Step 1: Login

Go to http://127.0.0.1:8000/docs and test the `/auth/login` endpoint:

```json
{
  "email": "superadmin@company.com",
  "password": "admin123"
}
```

You'll get a response like:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

## Step 2: Authorize

1. Click the "Authorize" button at the top right of Swagger UI
2. Paste the `access_token` value (without "bearer")
3. Click "Authorize" then "Close"

## Step 3: Test Endpoints

Now you can test any endpoint based on your role:

### SuperAdmin - Create Asset
```json
{
  "asset_tag": "LAP001",
  "asset_type": "Laptop",
  "brand": "Dell",
  "model": "XPS 15",
  "purchase_date": "2026-01-15",
  "department_id": 1
}
```

### IT Admin - Get Assets
GET `/itadmin/assets?status=AVAILABLE&page=1&size=20`

### IT Admin - Assign Asset
```json
{
  "asset_id": 1,
  "user_id": 4
}
```

### Employee - Request Asset
Login as employee first:
```json
{
  "email": "employee@company.com",
  "password": "employee123"
}
```

Then request:
```json
{
  "asset_type": "Laptop",
  "reason": "Need for development work"
}
```

### Employee - View My Assets
GET `/employee/my-assets`

## Complete Workflow Example

1. Login as SuperAdmin → Create Asset
2. Login as Employee → Request Asset
3. Login as IT Admin → Approve Request and Assign Asset
4. Login as Employee → View My Assets

## Available Test Users

| Role | Email | Password |
|------|-------|----------|
| SuperAdmin | superadmin@company.com | admin123 |
| IT Admin | itadmin@company.com | admin123 |
| Manager | manager@company.com | manager123 |
| Employee | employee@company.com | employee123 |
