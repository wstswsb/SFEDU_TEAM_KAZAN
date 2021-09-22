from models import User
from repositories import UserRepository
from exceptions import (
    NotFound,
    BadRequest
)


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository: UserRepository = repository

    def get_all(self) -> list[User]:
        users = self.repository.get_all()
        if users is None:
            raise NotFound()
        return users
