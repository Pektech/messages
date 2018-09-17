from app import app, ask, db, sup, ma
from .models import User, Family, Messages
from flask_ask import question
from flask_ask import session as ask_session
from flask import render_template
from sqlalchemy.exc import SQLAlchemyError
import logging
from .models import MessagesSchema

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
@sup.guide
def help_user():
    context_help = sup.get_help()
    return question(context_help)


@ask.launch
@sup.guide
def launched():
    ask_session.attributes['stage'] = 'start'
    ask_session.attributes['alexa_id'] = '999'  # hardcoded just for testing
    output = render_template('welcome')
    ask_session.attributes['last_speech'] = output
    return question(output)


@ask.intent('SayName')
@sup.guide
def my_name(name):
    if name is None:
        return sup.reprompt_error("I really need your name")
    my_name = name.capitalize()
    ask_session.attributes['my_name'] = my_name
    alexa_id = ask_session.attributes['alexa_id']
    # check if name in alexa_id family
    in_family = Family.query.filter(User.alexa_id == alexa_id,
                                    Family.name == my_name).first()
    if in_family is None:
        try:
            my_family = User.query.filter_by(alexa_id=alexa_id).first()
            add_name = Family(name=my_name, user_id=my_family.id)
            db.session.add(add_name)
            db.session.commit()
            print('added new family memeber')
        except SQLAlchemyError as e:
            db.session.rollback()

            print(e)
    output = render_template('name', my_name=my_name)
    ask_session.attributes['last_speech'] = output
    return question(output)


@ask.intent('CheckMessages')
#@sup.guide
def check_msg():
    my_name = ask_session.attributes['my_name']
    alexa_id = ask_session.attributes['alexa_id']
    my_family = User.query.filter_by(alexa_id=alexa_id).first()
    my_id: object = Family.query.filter(User.id == my_family.id,
                                        Family.name == my_name).first()

    my_msg_list = Messages.query.filter(Messages.to_id == my_id.id,
                                        Messages.deleted_flag == False) \
        .order_by(Messages.id.desc()).all()
    if len(my_msg_list) == 0:
        output = render_template('no_messages', my_name=my_name)
        ask_session.attributes['last_speech'] = output
        return question(output)
    # jsonify my_msg_list to store in alexa attributes
    msg_schema = MessagesSchema(many=True)
    msg_result = msg_schema.dump(my_msg_list)
    ask_session.attributes['my_msg_list'] = msg_result.data
    ask_session.attributes['msg_num'] = 0
    output = render_template('check_msg', name=my_name,
                                    count_msg=len(my_msg_list),
                                    my_msg_list=my_msg_list)
    ask_session.attributes['last_speech'] = output
    return question(output)


@ask.intent('NextMsg')
def next_msg():
    my_msg_list = ask_session.attributes['my_msg_list']
    msg_num = ask_session.attributes['msg_num'] +1
    if msg_num > len(my_msg_list) -1:
        output = render_template('end_of_messages')
        ask_session.attributes['last_speech'] = output
        return question(output)
    else:
        ask_session.attributes['msg_num'] = msg_num
        output = render_template('next_msg', my_msg_list=my_msg_list,
                                    msg_num=msg_num)
        ask_session.attributes['last_speech'] = output
        return question(output)


@ask.intent('AMAZON.YesIntent')
@sup.guide
def yesno():
    sup_state = sup.get_current_state()
    print(sup_state)



@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_speech = ask_session.attributes['last_speech']
    return question(repeat_speech)

def save_msg(msg, from_name, to_name):
    ''' will be converted into an intent - Saves message details to db'''
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
