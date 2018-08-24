"""
This file (test_models.py) contains the unit tests for the models.py file.
"""


def test_new_user(new_user):
    '''
    GIVEN a User model
    When a new User is created
    Then check alexa_id is defined correctly
    :param new_user:
    :return: string
    '''
    assert new_user.alexa_id == '999'

