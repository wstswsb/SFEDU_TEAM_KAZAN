from models import User
from .translator import Translator


class UsersTranslator(Translator):
    def from_document(self, mongo_user: dict) -> User:
        user = User()
        user.fullname = mongo_user.get("fullname")
        user.telegram_id = mongo_user.get("telegram_id")
        user.mongo_id = mongo_user.get("_id")
        return user

    def to_document(self, user: User) -> dict:
        return {
            "fullname": user.fullname,
            "telegram_id": user.telegram_id
        }
