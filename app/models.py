from app import db



family_mess = db.Table('family_mess',
                db.Column('family_id', db.Integer, db.ForeignKey('family.id')),
                db.Column('messages_id', db.Integer, db.ForeignKey('messages.id')))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alexa_id = db.Column(db.String(230), unique=True, nullable=False)

    family = db.relationship('Family', backref='user', lazy=True)



class Family(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(120))
    messages = db.relationship('Messages', backref='family', lazy=True)


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'))
    message = db.Column(db.Text(280))
    family_mess_table = db.relationship(
        'Messages', secondary=family_mess,
        primaryjoin=(family_mess.c.family_id==id),
        secondaryjoin=(family_mess.c.messages_id==id),
        backref=db.backref('family_mess', lazy='dynamic'), lazy='dynamic')


