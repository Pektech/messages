def test_app(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello Pek and Monk" in response.data