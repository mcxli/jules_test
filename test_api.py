from fastapi.testclient import TestClient
from main import app # Import the main FastAPI app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/v1/login", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}

def test_login_missing_username():
    response = client.post("/api/v1/login", json={"password": "testpassword"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username and password are required"}

def test_login_missing_password():
    response = client.post("/api/v1/login", json={"username": "testuser"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username and password are required"}

def test_login_empty_username():
    response = client.post("/api/v1/login", json={"username": "", "password": "testpassword"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username and password are required"}

def test_login_empty_password():
    response = client.post("/api/v1/login", json={"username": "testuser", "password": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username and password are required"}

def test_login_empty_credentials():
    response = client.post("/api/v1/login", json={"username": "", "password": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Username and password are required"}
