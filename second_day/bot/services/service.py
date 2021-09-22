from parsers import GetAllUsersParser
from requesters import UsersRequester
from models import User


class Service:
    def __init__(self, requester, parser) -> None:
        self.requester: UsersRequester = requester
        self.parser: GetAllUsersParser = parser

    def get_all_users(self) -> list[User]:
        users = self.parser.parse(self.requester.get_all_users())
        users = [User.from_request(data) for data in users]
        return users
