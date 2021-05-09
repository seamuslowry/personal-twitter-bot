from get_api.get_api import get_api

api = get_api()


def get_user_handler(handle):
    return api.get_user(handle)


def get_user():
    print('Enter a user identifier: ', end='')
    name = input()
    return get_user_handler(name)


def get_user_id():
    user = get_user()
    return user.id


if __name__ == '__main__':
    print(get_user_id())
