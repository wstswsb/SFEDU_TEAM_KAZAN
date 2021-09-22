import requests as rq
from requests import Response


class UsersRequester:
    def __init__(self, base_host: str) -> None:
        self.base_host: str = base_host

    def get_all_users(self) -> Response:
        url = f"{self.base_host}/users/all"
        users = rq.get(url)
        return users
