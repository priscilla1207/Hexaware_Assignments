import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/auth/login", json={
        "email": "admin@company.com",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_credentials():
    response = client.post("/auth/login", json={
        "email": "wrong@company.com",
        "password": "wrong"
    })
    assert response.status_code == 401
