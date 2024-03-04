from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_add_key():
    response = client.post(
        "/api/v1/add",
        json={"key": "test_key", "value": "test_value"}
    )
    assert response.status_code == 201
    print(response.json())
    assert response.json() == {
        "message": "Value added successfully"
    }


def test_add_existing_key():
    response = client.post(
        "/api/v1/add",
        json={"key": "test_key", "value": "test_value"}
    )
    assert response.status_code == 400
    assert response.json() == {
        "error": "Exception(\"Value with Key 'test_key' already exists.\")",
    }


def test_get_valid_key():
    response = client.get("/api/v1/get/test_key")
    assert response.status_code == 200
    assert response.json() == {
        "value": "test_value"
    }


def test_delete_valid_key():
    response = client.delete("/api/v1/delete/test_key")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {
        "message": "Value deleted successfully"
    }


def test_delete_invalid_key():
    response = client.delete("/api/v1/delete/test_key")
    assert response.status_code == 404
    assert response.json() == {
        "error": "Exception(\"Can't delete, key 'test_key' not found.\")"
    }


def test_get_invalid_key():
    response = client.get("/api/v1/get/test_key")
    assert response.status_code == 404
    assert response.json() == {
        "error": "Exception(\"Value with key 'test_key' not found.\")"
    }
