from pprint import pprint
from config import vkToken
import vk


def get_post():
    return 'рандомный пост мать его'


session = vk.Session(access_token=vkToken)
api = vk.API(session)
pprint(api.users.get(user_ids=1))
