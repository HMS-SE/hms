from fastapi.testclient import TestClient


def test_status(client: TestClient):
    response = client.get("/__status__")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
