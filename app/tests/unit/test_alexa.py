import json
from flask import url_for
from app.tests.fake_requests import *
from app.alexa import sup
import pytest


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


def test_name_is_sam(app, client):
    result = client.post('/', data=json.dumps(fake_say_name_Sam))
    assert result.status_code == 200
    data = json.loads(result.data.decode('utf-8'))
    print(data)
    assert 'Thank you Sam' in data['response']['outputSpeech']['text']


def test_check_msg_Bobby(app, client):
    result = client.post('/', data=json.dumps(fake_check_msg_Bobby))
    data = json.loads(result.data.decode('utf-8'))
    print(data['response']['outputSpeech']['text'])
    assert data['response']['outputSpeech']['text'] == \
           "Sorry Bobby there are no messages for you. Would you like to leave a message?"

@pytest.mark.skip(reason="only works if afg guide turned off")
def test_check_msg_Sam(app, client):

    result = client.post('/', data=json.dumps(test))

    data = json.loads(result.data.decode('utf-8'))
    print(sup.get_current_state())

    assert 'Okay  you have 2 messages.' in data['response']['outputSpeech']['text']


def test_next_msg(app, client):
    result = client.post('/', data=json.dumps(fake_next_msg))
    data = json.loads(result.data.decode('utf-8'))
    assert 'Need more apple pie' in data['response']['outputSpeech']['text']


def test_verify_is_off(app):
    app.config['ASK_VERIFY_REQUESTS'] = False

    assert app.config['ASK_VERIFY_REQUESTS'] == False