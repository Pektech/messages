import os

def test_app(client):
    '''
    Test that we are in the testing environment
    Test that flask is responding
    Test that flask return the correct page
    '''
    response = client.get('/')
    assert os.environ.get('FLASK_ENV') == 'testing'
    assert response.status_code == 200
    assert b"Hello Pek and Monk" in response.data