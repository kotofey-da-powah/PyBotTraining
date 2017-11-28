import json


def get_decoded_json(name):
    with open('{}.json'.format(name)) as file:
        encoded_coll = json.load(file)
    return encoded_coll


def encode_json(name, dictionary):
    with open('{}.json'.format(name), 'w') as file:
        json.dump(dictionary, file, ensure_ascii=False)
