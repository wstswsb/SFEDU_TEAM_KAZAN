from .mongo_repository import MongoRepository
from models import User


class UsersRepository(MongoRepository):

    def get_by_telegram_id(self, telegram_id: str) -> User:
        model = self.collection.find_one({"telegram_id": telegram_id})
        if not model:
            return None
        return self.translator.from_document(model)
