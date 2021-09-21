from .model import Model


class User(Model):
    def __init__(self) -> None:
        self.fullname: str = None
        self.telegram_id: str = None
        self.mongo_id: str = None

    @staticmethod
    def from_request(args: dict) -> "User":
        user = User()
        user.fullname = args.get("fullname")
        user.telegram_id = args.get("telegram_id")
        return user
