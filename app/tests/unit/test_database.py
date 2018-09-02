from app.models import User


def test_new_alexa_id(session):
    new_user = User(alexa_id='Monk_echo')

    session.add(new_user)
    session.commit()

    assert new_user.alexa_id == 'Ric_echo'
