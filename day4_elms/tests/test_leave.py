import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_apply_leave():
    # This test requires authentication token
    pass

def test_approve_leave():
    # This test requires authentication token
    pass
