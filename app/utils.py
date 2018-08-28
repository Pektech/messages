from flask import json
from .models import User, Family, Messages, MessagesSchema

def test():
    my_name = "Sam"
    alexa_id = '999'
    my_family = User.query.filter_by(alexa_id=alexa_id).first()
    my_id: object = Family.query.filter(User.id == my_family.id,
                                        Family.name == my_name).first()

    my_msg_list = Messages.query.filter(Messages.to_id == my_id.id,
                                        Messages.deleted_flag == False) \
        .order_by(Messages.id.desc()).all()
    test_json = json.dumps(item.as_dict() for item in my_msg_list)
    return test_json


def next_msg(order, msg_num=1):
    dean = Messages.query.filter_by(to_id=2).all()
    msg_all = MessagesSchema(many=True)
    dean_result = msg_all.dump(dean)
    test=dean_result


    current_msg = test.data[msg_num]['message']
    if order == 'next' and msg_num <= len(test.data):
        next_msg  = test.data[msg_num + 1]['message']
        print(next_msg)
        current_msg = next_msg
    elif order == 'next' and msg_num > len(test.data):
        print('end of messages')
    if order == 'repeat':
        print(current_msg)
