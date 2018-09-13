"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from app.alexa import my_name
import json
from flask import url_for
from app.tests.fake_requests import fake_say_name, fake_awake

fake_request =  {
  "version": "1.0",
  "session": {
    "new": True,
    "sessionId": "amzn1.echo-api.session.0000000-0000-0000-0000-00000000000",
    "application": {
      "applicationId": "fake-application-id"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.account.AM3B00000000000000000000000"
    }
  },
  "context": {
    "System": {
      "application": {
        "applicationId": "fake-application-id"
      },
      "user": {
        "userId": "amzn1.account.AM3B00000000000000000000000"
      },
      "device": {
        "supportedInterfaces": {
          "AudioPlayer": {}
        }
      }
    },
    "AudioPlayer": {
      "offsetInMilliseconds": 0,
      "playerActivity": "IDLE"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "string",
    "timestamp": "string",
    "locale": "string",
    "intent": {
      "name": "SayName",
      "slots": {"name":
                    {"name": "name",
                     "confirmationStatus": "NONE"}
        }
      },"dialogState": "STARTED"
    }
}



def test_new_user(new_user):
    '''
    GIVEN a User model
    When a new User is created
    Then check alexa_id is defined correctly
    :param new_user:
    :return: string
    '''
    assert new_user.alexa_id == '999'



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
