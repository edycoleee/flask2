import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_register_success(client):
    response = client.post('/register', json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 201
    assert response.get_json()["message"] == "Registrasi berhasil"

def test_register_duplicate(client):
    # Register pertama kali
    client.post('/register', json={
        "username": "testuser",
        "password": "testpass"
    })

    # Register ulang dengan username yang sama
    response = client.post('/register', json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 409
    assert response.get_json()["error"] == "Username sudah digunakan"

def test_register_missing_fields(client):
    response = client.post('/register', json={
        "username": "incomplete"
        # password tidak dikirim
    })
    assert response.status_code == 400
    assert "wajib diisi" in response.get_json()["error"]