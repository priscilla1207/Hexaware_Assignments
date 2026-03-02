import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_asset_unauthorized():
    response = client.post("/itadmin/assets", json={
        "asset_tag": "LAP001",
        "asset_type": "Laptop",
        "brand": "Dell"
    })
    assert response.status_code == 401

def test_create_asset_duplicate_tag():
    # This test requires authentication token
    pass
