from get_api.get_api import get_api

api = get_api()


def get_user_id(handle):
    return api.get_user(handle)

def get_user_id():
    print('Enter a user identifier: ')
    name = input()
    return get_user_id(name)


if __name__ == '__main__':
    get_user_id()