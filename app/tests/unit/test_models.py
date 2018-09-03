"""
This file (test_models.py) contains the unit tests for the models.py file.
"""
from app.alexa import my_name

def test_new_user(new_user):
    '''
    GIVEN a User model
    When a new User is created
    Then check alexa_id is defined correctly
    :param new_user:
    :return: string
    '''
    assert new_user.alexa_id == '999'



def test_name_is_blank(app):
    app.config['ASK_VERIFY_REQUESTS'] = False
    name=""
    result = my_name(name)
    data = result._response

    assert data['text']=="I really need your name"


def test_verrify_is_off(app):
    app.config['ASK_VERIFY_REQUESTS'] = False

    assert app.config['ASK_VERIFY_REQUESTS'] == False
