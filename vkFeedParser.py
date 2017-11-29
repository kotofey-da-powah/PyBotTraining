from pprint import pprint
import random

import vk_api

from config import vkToken
import json_serializer


def get_updates():
    """Get last ~1000 posts about #python"""

    MAX_COUNT = 200            #max count of posts per request
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
    """Creates clear list of posts containing only text and url"""

    MIN_LIKES = 500                      #min amount of likes for filter

    wet_list = []
    url_pattern = 'https://vk.com/wall'  # .../wall+[from_id]+[id] pattern

    for post in raw_list:           
        if 'copy_history' in post:       #skip reposted
            continue

        if post['likes']['count'] > MIN_LIKES:
            url = '{}{}_{}'.format(url_pattern, post['from_id'], post['id'])#building url
            wet_post = {
                'url': url,
                'text': post['text']     #building post
            }
            wet_list += [wet_post]
    return wet_list


def write_to_json(post_list):
    """Complete posts.json with new posts"""
    pres_posts = json_serializer.get_decoded_json('posts')
    clear = check_simil(pres_posts, post_list) #check for similar posts
    new_posts = pres_posts + clear
    json_serializer.encode_json('posts', new_posts)


def check_simil(original_list, lists_to_write):
    """Checking similar posts in previous list"""
    clear_list = []
    for writing_post in lists_to_write:
        originaд_texts = [or_post['text'] for or_post in original_list]
        if not(writing_post['text'] in originaд_texts):
            clear_list += [writing_post]
    return clear_list


def update():
    try:
        write_to_json(build_list((get_updates())))
    except FileNotFoundError:    #error for not existing posts.json
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
