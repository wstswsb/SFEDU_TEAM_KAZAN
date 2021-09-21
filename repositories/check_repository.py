from .mongo_repository import MongoRepository
from models import Check


class CheckRepository(MongoRepository):
    def get_history(self, telegram_owner_id: str) -> list[Check]:
        checks = self.collection.find(
            {
                "telegram_owner_id": telegram_owner_id
            }).limit(10)
        return [self.translator.from_document(check) for check in checks]

    def update_by_telegram_img_id(self, model: Check) -> str:
        self.collection.update_one(
            {"telegram_img_id": model.telegram_img_id},
            {"$set": self.translator.to_document(model)}
        )
        return model

    def get_by_telegram_img_id(self, telegram_img_id: str) -> Check:
        check = self.collection.find_one({"telegram_img_id": telegram_img_id})
        if check is None:
            return None
        return self.translator.from_document(check)
