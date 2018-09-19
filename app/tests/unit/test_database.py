from app.models import User
from app.alexa import save_msg
import pytest

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
    save_msg('need apples', 'Pek')
    query_db = User.query.filter(alexa_id==alexa_id).first()
    assert any(x.name =='Pek' for x in query_db.family_members)

