import os

def test_app(client):
    response = client.get('/')
    assert os.environ.get('FLASK_ENV') == 'testing'
    assert response.status_code == 200
    assert b"Hello Pek and Monk" in response.data