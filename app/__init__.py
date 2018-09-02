import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_ask import Ask
from afg import Supervisor
from flask_marshmallow import Marshmallow

config = {
    "dev": "config.DevConfig",
    "testing": "config.TestConfig",
    "default": "config.DevConfig"
        }
config_name = os.getenv('FLASK_ENV', 'default')



app = Flask(__name__)
app.config.from_object(config[config_name])
print(config_name)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ask = Ask(app, '/')
sup = Supervisor('app/scenario.yaml')
ma = Marshmallow(app)

from app import routes, models, alexa

# @app.route("/")
# def hello():
#     return "Hello World!"