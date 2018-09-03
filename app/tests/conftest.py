import sys
import pytest
import os
import messages
from app import db as _db , sup as _sup
from sqlalchemy import event
from sqlalchemy.orm import sessionmaker
from app.models import User


os.environ["FLASK_ENV"] = 'testing'
#this is where we set up pytest fixtures
# @pytest.fixture(scope='module')
# def new_user():
#     user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
#     return user




@pytest.fixture(scope='module')
def new_user():
    user = User(alexa_id='999')
    return user

@pytest.fixture(scope='session')
def suptest():
    @_sup.start
    def new_session():
        app.logger.debug('new user session started')



@pytest.fixture(scope='session')
def app():

    return messages.app


@pytest.fixture(scope="session")
def db(app, request):
    """
    Returns session-wide initialised database.
    """
    with app.app_context():
        _db.drop_all()
        _db.create_all()



@pytest.fixture(scope="function", autouse=True)
def session(app, db, request):
    """
    Returns function-scoped session.
    """
    with app.app_context():
        conn = _db.engine.connect()
        txn = conn.begin()

        options = dict(bind=conn, binds={})
        sess = _db.create_scoped_session(options=options)

        # # establish  a SAVEPOINT just before beginning the test
        # # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
        # sess.begin_nested()
        #
        # @event.listens_for(sess(), 'after_transaction_end')
        # def restart_savepoint(sess2, trans):
        #     # Detecting whether this is indeed the nested transaction of the test
        #     if trans.nested and not trans._parent.nested:
        #         # The test should have normally called session.commit(),
        #         # but to be safe we explicitly expire the session
        #         sess2.expire_all()
        #         sess.begin_nested()

        _db.session = sess
        yield sess

        # Cleanup
        sess.remove()
        # This instruction rollsback any commit that were executed in the tests.
        txn.rollback()
        conn.close()