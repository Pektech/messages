from app.models import User, Messages, Family
from app.alexa import save_msg
import pytest
from app.tests.conftest import fake_session
from unittest.mock import MagicMock

def test_new_alexa_id(session):
    '''Test that a new test database is set up'''
    new_user = User(alexa_id='Monk_echo')

    session.add(new_user)
    session.commit()

    assert new_user.alexa_id == 'Monk_echo'

@pytest.mark.usefixtures('session')
def test_adds_new_family_member():

    alexa_id = '999'
    my_name = 'Sam'

    save_msg('need apples', 'Harry')
    query_db = User.query.filter(alexa_id==alexa_id).first()
    assert any(x.name =='Harry' for x in query_db.family_members)

@pytest.mark.usefixtures('session')
def test_leaves_message():
    alexa_id = '999'
    my_name = 'Sam'
    save_msg('need apples', 'Harry')
    family_id = User.query.filter_by(alexa_id=alexa_id).first()
    goes_to = Family.query.filter(Family.user_id == family_id.id,
                                  Family.name == "Harry").first()
    msg_query = Messages.query.filter_by(to_id=goes_to.id).order_by(
            Messages.id.desc()).first()
    assert "need apples" in msg_query.message


@pytest.mark.usefixtures('fake_session')
def test_fake_session():
    fake = fake_session()
    assert fake.attributes['alexa_id'] == '999'