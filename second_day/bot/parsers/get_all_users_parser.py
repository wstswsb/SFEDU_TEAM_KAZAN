from requests import Response
from exceptions import NotFound


class GetAllUsersParser:
    def parse(self, users: Response) -> list[dict]:
        if users.status_code == 404:
            raise NotFound
        return users.json()
