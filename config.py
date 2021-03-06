import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'monkey-keeps-the-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir,
                                                          'messages.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_DEBUG=0
    DEBUG = False


class DevConfig(Config):
    FLASK_DEBUG = 0
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                                                          'test_db.db')

    TESTING = True
    DEBUG = True
    ASK_VERIFY_REQUESTS = False