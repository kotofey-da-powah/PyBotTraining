"""Init (reset) posts.json"""


def init():
    try:
        with open('posts.json') as file:
            container = file.read()
        with open('posts_backup.json', 'w') as file:
            file.write(container)
        print('Previous list saved to posts_backup.json')
    except FileNotFoundError:
        pass
    with open('posts.json', 'w') as file:
        file.write('[]')
    print('Done!')


def restore():
    with open('posts_backup.json') as file:
        container = file.read()
    with open('posts.json', 'w') as file:
        file.write(container)
    print("Restored!")


def main():
    answer = input('(I)nitialize or (R)estore: ')
    if answer.lower() == 'i':
        init()
    elif answer.lower() == 'r':
        restore()


if __name__ == '__main__':
    main()
