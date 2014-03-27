import json
import os

__filename__ = 'context.json'


def read():
    pass


class Config:
    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password = password

    def auth(self):
        return (self.username, self.password)

    def baseurl(self):
        return 'https://historical.gnip.com/accounts/{account}'.format(
            account=self.account
        )

# def config(account, username, password):
#     return {
#         'account': account,
#         'username': username,
#         'password': password,
#     }


def config_exists():
    return os.path.isfile(__filename__)


def read_context():
    try:
        with open(__filename__) as f:
            return json.load(f)
    except IOError:
        return None
        # init_context()


def store_context(data, force=False):
    if force:
        mode = 'w+'
    else:
        mode = 'w'

    with open(__filename__, mode) as f:
        json.dump(data, f)
