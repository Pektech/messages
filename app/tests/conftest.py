import sys
import pytest


from app.models import User

#this is where we set up pytest fixtures
# @pytest.fixture(scope='module')
# def new_user():
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     return user




@pytest.fixture(scope='module')
def new_user():
    user = User(alexa_id='999')
    return user


import pytest
import os
import messages


@pytest.fixture
def app():
    return messages.app


@pytest.fixture(scope='module')
def init_database():
    pass

