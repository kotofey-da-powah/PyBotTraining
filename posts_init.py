"""Init (reset) posts.json"""


def main():
    with open('posts.json', 'w') as file:
        file.write('[]')

if __name__ == '__main__':
    main()