# app/tests/test_main.py

from fastapi.testclient import TestClient
from app import *
import pytest

# PyTest fixtures
@pytest.fixture
def client():
    """Create a TestClient instance for testing."""
    return TestClient(app)

# PyTest functions
def test_read_main(client):
    """Test the root endpoint ("/")."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_main_invalid_path(client):
    """Test an invalid path."""
    response = client.get("/invalid_path")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}