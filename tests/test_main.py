from fastapi.testclient import TestClient
from app.main import __version__
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

# TODO (PROJ-101): add a test for GET /health here.

def test_read_root():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": __version__}

