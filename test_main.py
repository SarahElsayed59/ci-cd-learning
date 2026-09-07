from fastapi.testclient import TestCleint
from main import app

client=TestCleint()


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}