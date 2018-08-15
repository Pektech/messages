from app import ask, db
from .models import User, Family, Messages







def save_msg(msg, from_name, to_name):
    ''' will be converted into an intent - Saves message details to db'''
    alexa = '999' #would need to pull from intent atributes
    family_id = User.query.filter_by(alexa_id=alexa).first()
    came_from = Family.query.filter(Family.user_id==family_id.id,
                                  Family.name == from_name).first()
    goes_to = Family.query.filter(Family.user_id==family_id.id,
                                  Family.name == to_name).first()
    text = Messages(from_id=came_from.id, message=msg, to_id=goes_to.id)
    try:
        db.session.add(text)
        db.session.commit()
        print('msg added')
    except:
        db.session.rollback()
        print('something went wrong')



def delete_msg(msg, to_name):
    ''' will be converted into an intent - Delete message details to db'''
    alexa = '999'  # would need to pull from intent atributes
    family_id = User.query.filter_by(alexa_id=alexa).first()
    came_from = Family.query.filter(Family.user_id == family_id.id,
                                    Family.name == from_name).first()
    goes_to = Family.query.filter(Family.user_id == family_id.id,
                                  Family.name == to_name).first()
    text = Messages(from_id=came_from.id, message=msg, to_id=goes_to.id)
    try:
        db.session.add(text)
        db.session.commit()
        print('msg added')
    except:
        db.session.rollback()
        print('something went wrong')