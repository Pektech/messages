from flask import json
from .models import User, Family, Messages

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


def next_msg(next):
    test = [{'fam_sent': 1, 'deleted_flag': False, 'fam_to': 2, 'message': 'werewoves and vamps', 'id': 5}, {'fam_sent': 1, 'deleted_flag': False, 'fam_to': 2, 'message': 'Want me to bring home pie?', 'id': 2}, {'fam_sent': 1, 'deleted_flag': False, 'fam_to': 2, 'message': 'hey just off to the library', 'id': 1}]

    msg_num = 0
    first_msg = test[0]['message']
    if next == 'next' and msg_num <= len(test.data):
        next_msg  = test[msg_num + 1]['message']
        print(next_msg)
