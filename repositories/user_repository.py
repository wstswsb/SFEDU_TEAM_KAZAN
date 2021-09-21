from bson import ObjectId
from .mongo_repository import MongoRepository
from models import User


class UsersRepository(MongoRepository):

    def get_by_telegram_id(self, telegram_id: str) -> User:
        model = self.collection.find_one({"telegram_id": telegram_id})
        if model is None:
            return None
        return self.translator.from_document(model)

    def create(self, user: User) -> ObjectId:
        model = self.get_by_telegram_id(user.telegram_id)
        if model is not None:
            return None
        return super().create(user)
