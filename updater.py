from vkFeedParser import update


def main():
    if input('For update type (up): ') == 'up':
        response = update()
        if response == 0:
            print('Updated!')
        else:
            print(response)


if __name__ == '__main__':
    main()