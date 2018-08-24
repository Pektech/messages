from app import app, db, ma
from app.models import User, Family, Messages



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Family': Family, 'Messages': Messages,
            'ma': ma}

