#/test/test_siswa.py
# client >> function test >> get(url) >> assert response
import pytest
from app import app

# membuat object client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_all_siswa(client):
    # method (url)
    response = client.get('/siswa')
    # assert >> code success >> 200
    assert response.status_code == 200
    json_data = response.get_json()

    assert json_data['message'] == "Daftar siswa berhasil diambil"
    # assert >> berupa json >> list
    assert isinstance(json_data['data'], list)