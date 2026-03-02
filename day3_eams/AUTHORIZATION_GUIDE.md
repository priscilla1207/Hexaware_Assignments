# Complete Authorization & Testing Guide

## Step-by-Step: How to Authorize in Swagger UI

### Step 1: Login to Get Token

1. Go to http://127.0.0.1:8000/docs
2. Find the **POST /auth/login** endpoint under "Authentication"
3. Click "Try it out"
4. Replace the JSON with:

```json
{
  "email": "superadmin@company.com",
  "password": "admin123"
}
```

5. Click "Execute"
6. You'll get a response like:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzdXBlcmFkbWluQGNvbXBhbnkuY29tIiwicm9sZSI6IlNVUEVSQURNSU4iLCJleHAiOjE3MDk0NzY4MDB9.abc123...",
  "token_type": "bearer"
}
```

7. **COPY the entire access_token value** (the long string)

### Step 2: Authorize in Swagger UI

1. Look at the TOP RIGHT of the Swagger page
2. Click the **"Authorize"** button (it has a lock icon 🔒)
3. A popup will appear with a field labeled "Value"
4. **PASTE the access_token** you copied (just the token, not "bearer")
5. Click **"Authorize"** button in the popup
6. Click **"Close"**
7. You'll see the lock icon is now LOCKED 🔒 (filled)

### Step 3: Test Protected Endpoints

Now you can test any endpoint! The token is automatically included in all requests.

---

## JSON Examples for All Endpoints

### 1. SuperAdmin Endpoints

#### Create Department
**POST /superadmin/departments**
```json
{
  "name": "Engineering",
  "manager_id": 3
}
```

#### Create User
**POST /superadmin/users**
```json
{
  "name": "John Doe",
  "email": "john.doe@company.com",
  "role": "EMPLOYEE",
  "department_id": 1,
  "password": "password123"
}
```

Another example - Create IT Admin:
```json
{
  "name": "Jane Smith",
  "email": "jane.smith@company.com",
  "role": "IT_ADMIN",
  "department_id": 1,
  "password": "admin456"
}
```

Another example - Create Manager:
```json
{
  "name": "Bob Manager",
  "email": "bob.manager@company.com",
  "role": "MANAGER",
  "department_id": 2,
  "password": "manager456"
}
```

#### Create Asset
**POST /superadmin/assets**
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

More asset examples:
```json
{
  "asset_tag": "MON001",
  "asset_type": "Monitor",
  "brand": "LG",
  "model": "UltraWide 34",
  "purchase_date": "2026-02-01",
  "department_id": 1
}
```

```json
{
  "asset_tag": "MOB001",
  "asset_type": "Mobile",
  "brand": "Apple",
  "model": "iPhone 15 Pro",
  "purchase_date": "2026-01-20",
  "department_id": 2
}
```

```json
{
  "asset_tag": "LIC001",
  "asset_type": "License",
  "brand": "Microsoft",
  "model": "Office 365",
  "purchase_date": "2026-01-01",
  "department_id": 1
}
```

```json
{
  "asset_tag": "VEH001",
  "asset_type": "Vehicle",
  "brand": "Toyota",
  "model": "Camry 2026",
  "purchase_date": "2025-12-15",
  "department_id": 3
}
```

---

### 2. IT Admin Endpoints

#### Create Asset
**POST /itadmin/assets**
```json
{
  "asset_tag": "LAP002",
  "asset_type": "Laptop",
  "brand": "HP",
  "model": "EliteBook 840",
  "purchase_date": "2026-02-10",
  "department_id": 2
}
```

#### Get Assets (with filters)
**GET /itadmin/assets**

Query parameters:
- status: AVAILABLE
- page: 1
- size: 20

Or try:
- status: ASSIGNED
- page: 1
- size: 10

#### Assign Asset
**POST /itadmin/assignments**
```json
{
  "asset_id": 1,
  "user_id": 4
}
```

Note: 
- asset_id: Use the ID from an asset you created
- user_id: Use ID 4 (employee) or any employee user ID

---

### 3. Employee Endpoints

**First, logout and login as employee:**

**POST /auth/login**
```json
{
  "email": "employee@company.com",
  "password": "employee123"
}
```

Then authorize with the new token.

#### Request Asset
**POST /employee/requests**
```json
{
  "asset_type": "Laptop",
  "reason": "Need for development work on new project"
}
```

Another example:
```json
{
  "asset_type": "Monitor",
  "reason": "Current monitor is too small for design work"
}
```

#### View My Assets
**GET /employee/my-assets**

No body needed, just click Execute.

---

### 4. Manager Endpoints

**First, logout and login as manager:**

**POST /auth/login**
```json
{
  "email": "manager@company.com",
  "password": "manager123"
}
```

#### View Department Assets
**GET /manager/department-assets**

No body needed, just click Execute.

---

## Complete Workflow Test

### Scenario: Employee Requests and Gets a Laptop

1. **Login as SuperAdmin**
```json
{
  "email": "superadmin@company.com",
  "password": "admin123"
}
```
Authorize with token.

2. **Create Asset**
POST /superadmin/assets
```json
{
  "asset_tag": "LAP100",
  "asset_type": "Laptop",
  "brand": "Lenovo",
  "model": "ThinkPad X1",
  "purchase_date": "2026-03-01",
  "department_id": 2
}
```
Note the asset ID from response (e.g., id: 1)

3. **Logout and Login as Employee**
```json
{
  "email": "employee@company.com",
  "password": "employee123"
}
```
Authorize with new token.

4. **Request Asset**
POST /employee/requests
```json
{
  "asset_type": "Laptop",
  "reason": "Need for remote work setup"
}
```
Note the request ID from response (e.g., id: 1)

5. **Logout and Login as IT Admin**
```json
{
  "email": "itadmin@company.com",
  "password": "admin123"
}
```
Authorize with new token.

6. **Assign Asset to Employee**
POST /itadmin/assignments
```json
{
  "asset_id": 1,
  "user_id": 4
}
```

7. **Logout and Login as Employee Again**
```json
{
  "email": "employee@company.com",
  "password": "employee123"
}
```
Authorize with new token.

8. **View My Assets**
GET /employee/my-assets

You should see the laptop assigned to you!

---

## Valid Role Values

When creating users, use these exact role values:
- `SUPERADMIN`
- `IT_ADMIN`
- `MANAGER`
- `EMPLOYEE`

## Valid Asset Types

- `Laptop`
- `Monitor`
- `Mobile`
- `License`
- `Vehicle`

## Valid Asset Status Values

- `AVAILABLE`
- `ASSIGNED`
- `MAINTENANCE`
- `RETIRED`
