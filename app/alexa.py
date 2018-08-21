from app import ask, db, sup, app
from .models import User, Family, Messages
from flask_ask import statement, question, context, delegate
from flask_ask import session as ask_session, request as ask_request
from flask import render_template
from sqlalchemy import func
import logging

logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.on_session_started
@sup.start
def new_session():
    app.logger.debug('new user session started')


@sup.stop
def close_user_session():
    app.logger.debug("user session stopped")


@ask.session_ended
def session_ended():
    close_user_session()
    return '', 200

@ask.intent('AMAZON.HelpIntent')
def help_user():
    context_help = sup.get_help()
    return question(context_help)




@ask.launch
@sup.guide
def launched():
    ask_session.attributes['stage'] = 'start'
    ask_session.attributes['alexa_id'] = '999' #hardcoded just for testing
    return question(render_template('welcome'))

@ask.intent('SayName')
@sup.guide
def from_name(from_name):

    ask_session.attributes['from_name'] = from_name
    return question(render_template('name', name=from_name))




@ask.intent('CheckMessages')
@sup.guide
def check_msg():
    from_name = ask_session.attributes['from_name']
    alexa_id = ask_session.attributes['alexa_id']
    my_family = User.query.filter_by(alexa_id=alexa_id).first()
    my_id = Family.query.filter(User.id==my_family.id,
                                Family.name==from_name).first()

    my_msg_list = Messages.query.filter(Messages.to_id== my_id.user_id,
                                        Messages.deleted_flag == False).all()

    print(len(my_msg_list))
    return question(render_template('check_msg', name=from_name,
                                    count_msg=len(my_msg_list)))


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