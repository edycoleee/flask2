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

def test_create_siswa(client):
    response = client.post('/siswa', json={"nama": "Silmi", "alamat": "Semarang"})
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data['message'] == "Siswa berhasil ditambahkan"
    assert json_data['data']['nama'] == "Silmi"
    assert json_data['data']['alamat'] == "Semarang"
    assert isinstance(json_data['data']['id'], int)

from unittest.mock import patch

# Test gagal insert karena data kosong atau field tidak lengkap
def test_create_siswa_gagal_validasi(client):
    # data kosong
    response = client.post('/siswa', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Field 'nama' dan 'alamat' wajib diisi"

    # hanya ada nama
    response = client.post('/siswa', json={"nama": "Silmi"})
    assert response.status_code == 400

    # hanya ada alamat
    response = client.post('/siswa', json={"alamat": "Jakarta"})
    assert response.status_code == 400

# Test gagal insert karena terjadi exception di service
def test_create_siswa_gagal_exception(client):
    with patch('services.siswa_service.create_siswa', side_effect=Exception("DB error")):
        response = client.post('/siswa', json={"nama": "Silmi", "alamat": "Semarang"})
        assert response.status_code == 500
        assert response.get_json()['error'] == "Gagal menambahkan siswa"

def test_read_siswa_by_id(client):
    # Tambahkan siswa dulu
    create_response = client.post('/siswa', json={"nama": "Coba", "alamat": "Bandung"})
    siswa_id = create_response.get_json()['data']['id']

    # Baca siswa yang sudah dibuat
    response = client.get(f'/siswa/{siswa_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Data siswa ditemukan"
    assert json_data['data']['id'] == siswa_id
    assert json_data['data']['nama'] == "Coba"
    assert json_data['data']['alamat'] == "Bandung"

    # Test siswa yang tidak ada
    response_404 = client.get('/siswa/999999')
    assert response_404.status_code == 404
    assert response_404.get_json()['error'] == "Siswa dengan ID tersebut tidak ditemukan"

def test_delete_siswa(client):
    # Tambahkan siswa terlebih dahulu
    create_response = client.post('/siswa', json={"nama": "Delete Me", "alamat": "Nowhere"})
    siswa_id = create_response.get_json()['data']['id']

    # Lakukan DELETE
    response = client.delete(f'/siswa/{siswa_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['message'] == "Siswa berhasil dihapus"
    assert json_data['data']['id'] == siswa_id

    # DELETE lagi → harusnya 404
    response_2 = client.delete(f'/siswa/{siswa_id}')
    assert response_2.status_code == 404
    assert response_2.get_json()['error'] == "Siswa dengan ID tersebut tidak ditemukan"