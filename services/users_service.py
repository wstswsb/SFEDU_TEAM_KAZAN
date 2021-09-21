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
        return user
