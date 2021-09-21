from models.check import Check
from bson.objectid import ObjectId
from .check_service import CheckService
from exceptions import (
    NotFound,
    Conflict
)
from repositories import UsersRepository
from models import User


class UsersService:
    def __init__(self, repository: UsersRepository) -> None:
        self.repository: UsersRepository = repository

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

    def upload_user_check(self, args: dict) -> Check:
        check = self.check_service.upload(args)
        return check
