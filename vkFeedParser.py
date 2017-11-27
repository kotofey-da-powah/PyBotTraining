from pprint import pprint

import vk_api

from config import vkToken


def get_updates():
    session = vk_api.VkApi(token=vkToken)
    api = session.get_api()

    response = api.newsfeed.search(q='#python', count=200)
    posts = response['items']
    while 'next_from' in response:
        response = api.newsfeed.search(q='#python', count=200, start_from=response['next_from'])
        posts += response['items']

    return posts


def build_list(raw_list):
    liked = 0
    for post in raw_list:
        if post['likes']['count'] > 1000:
            liked += 1
    print(liked)


def get_post():
    return 'рандомный пост мать его'


def main():
    build_list((get_updates()))


if __name__ == '__main__':
    main()
