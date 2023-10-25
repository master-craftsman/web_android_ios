from . import env

DEFAULT_LOGIN = env.get('DEFAULT_LOGIN', 'test-arman@bind.com')
DEFAULT_PASSWORD = env.get('DEFAULT_PASSWORD', 'Testtest')

USERS = {
    'default': {
        'password': DEFAULT_PASSWORD,
        'email': DEFAULT_LOGIN,
    },
}


def get_user(user):
    _user = USERS.get(user)
    if not _user:
        raise ValueError('Undefined user name')
    return _user
