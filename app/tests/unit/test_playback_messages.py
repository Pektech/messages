from app.utils import next_msg
import pytest

msg_list = [
    {'fam_sent': 1, 'deleted_flag': False, 'fam_to': 2,
     'message': 'hey just off to the library', 'id': 1},
    {'fam_sent': 1, 'deleted_flag': False, 'fam_to': 2,
     'message': 'Want me to bring home pie?', 'id': 2},
    {'fam_sent': 1, 'deleted_flag': False, 'fam_to': 2,
     'message': 'werewoves and vamps', 'id': 5}]

@pytest.mark.usefixtures('session')
class Test:



    # @pytest.mark.parametrize('order, msg_num, message' ,[
    #     ('next', 0, 'hey just off to the library'),
    #     ('next', 1, 'Want me to bring home pie?'),
    #     ('next', 2, 'werewoves and vamps')])
    #
    # def test_next_msg(self,order, msg_num, message):
    #     result = next_msg(order, msg_num)
    #     assert result == message

    def test_next_msg(self):
        result = next_msg()




