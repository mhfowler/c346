from hello_app.arena.search import Search
from .blocks import Blocks
from .channels import Channels
from .feed import Feed
from .users import Users


class Arena():
    def __init__(self, access_token):
        self.access_token = access_token
        self.users = Users(access_token=access_token)
        self.blocks = Blocks(access_token=access_token)
        self.channels = Channels(access_token=access_token)
        self.feed = Feed(access_token=access_token)
        self.search = Search()
