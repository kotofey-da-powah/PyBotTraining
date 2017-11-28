from pprint import pprint
import random

import vk_api

from config import vkToken
import json_serializer


def get_updates():
    MAX_COUNT = 200
    session = vk_api.VkApi(token=vkToken)
    api = session.get_api()
    response = api.newsfeed.search(q='#python', count=MAX_COUNT)
    posts = list(response['items'])
    while 'next_from' in response:
        response = api.newsfeed.search(
            q='#python', count=MAX_COUNT, start_from=response['next_from'])
        posts += response['items']
    return posts


def build_list(raw_list):
    MIN_LIKES = 500

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
    clear = check_simil(pres_posts, post_list)
    new_posts = pres_posts + clear
    json_serializer.encode_json('posts', new_posts)


def check_simil(original_list, lists_to_write):
    clear_list = []
    for writing_post in lists_to_write:
        originaд_texts = [or_post['text'] for or_post in original_list]
        if not(writing_post['text'] in originaд_texts):
            clear_list += [writing_post]
    return clear_list


def update():
    try:
        write_to_json(build_list((get_updates())))
    except FileNotFoundError:
        print('No posts.json file found, run posts_init.py')


def get_random_post():
    posts = json_serializer.get_decoded_json('posts')
    rnd = random.randint(0, len(posts) - 1)
    return posts[rnd]


def main():
    if input('For update type (up): ') == 'up':
        update()


if __name__ == '__main__':
    main()
