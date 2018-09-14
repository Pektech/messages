import json
from flask import url_for
from app.tests.fake_requests import fake_say_name, fake_awake


def  test_alexa_wakes(app, client):
    result = client.post('/', data=json.dumps(fake_awake))
    data = json.loads(result.data.decode('utf-8'))
    print(data)
    assert data['response']['outputSpeech']['text'] == "Welcome to Family Messages. " \
                                                       "Will you please tell me your name?"




def test_name_is_blank(app, client):
    result = client.post('/', data=json.dumps(fake_say_name))
    assert result.status_code == 200
    data = json.loads(result.data.decode('utf-8'))
    print(data)
    assert data['response']['outputSpeech']['text']=="I really need your name"


def test_verify_is_off(app):
    app.config['ASK_VERIFY_REQUESTS'] = False

    assert app.config['ASK_VERIFY_REQUESTS'] == False