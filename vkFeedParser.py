from pprint import pprint

import vk

from config import vkToken

session = vk.Session(access_token=vkToken)
api = vk.API(session)
pprint(api.users.get(user_ids=1))
