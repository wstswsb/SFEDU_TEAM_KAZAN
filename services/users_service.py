from exceptions.not_found import NotFound
from pymongo.common import raise_config_error
from exceptions.conflict import Conflict
from repositories import UsersRepository
from models import User


class UsersService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    def create(self, args: dict) -> User:
        user = User.from_request(
            {
                "fullname": args.get("fullname"),
                "telegram_id": args.get("telegram_id")
            }
        )
        user.mongo_id = self.repository.create(user)
        if user.mongo_id is None:
            raise Conflict()
        return user

    def get_by_telegram_id(self, args: dict) -> User:
        user = self.repository.get_by_telegram_id(args.get("telegram_id"))
        if user is None:
            raise NotFound()
        return user
