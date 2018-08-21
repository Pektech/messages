from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_ask import Ask
from afg import Supervisor


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ask = Ask(app, '/')
sup = Supervisor('app/scenario.yaml')

from app import routes, models, alexa

