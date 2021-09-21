from models import User


class UsersPresenter:

    def to_json(self, user: User) -> dict:
        return {
            "fullname": user.fullname,
            "telegram_id": user.telegram_id,
            "mongo_id": str(user.mongo_id)
        }
