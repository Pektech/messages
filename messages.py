from app import app, db
from app.models import User, Family, Messages, family_mess



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Family': Family, 'Messages': Messages,
            'family_mess': family_mess}

