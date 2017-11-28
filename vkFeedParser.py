from pprint import pprint

import vk_api

from config import vkToken
import json_serializer


def get_updates():
    MAX_COUNT = 50
    session = vk_api.VkApi(token=vkToken)
    api = session.get_api()
    response = api.newsfeed.search(q='#python', count=MAX_COUNT)
    posts = list(response['items'])
    # while 'next_from' in response:
    #    response = api.newsfeed.search(
    #        q='#python', count=MAX_COUNT, start_from=response['next_from'])
    #    posts += response['items']
    return posts


def build_list(raw_list):
    MIN_LIKES = 250

    wet_list = []
    url_pattern = 'https://vk.com/wall'  # .../wall+from_id+id

    for post in raw_list:
        if 'copy_history' in post:
            continue

        if post['likes']['count'] > MIN_LIKES:
            url = '{}{}_{}'.format(url_pattern, post['from_id'], post['id'])
            wet_post = {
                'url': url,
                'text': post['text']
            }
            wet_list += [wet_post]
    return wet_list


def write_to_json(post_list):
    pres_posts = json_serializer.get_decoded_json('posts')
    new_posts = pres_posts + post_list
    json_serializer.encode_json('posts',new_posts)


def get_post():
    return 'рандомный пост мать его'


def main():
    write_to_json(build_list((get_updates())))


if __name__ == '__main__':
    main()
