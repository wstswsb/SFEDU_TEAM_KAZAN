from .translator import Translator
from models import Check


class CheckTranslator(Translator):
    def to_document(self, model: Check) -> dict:
        return {
            "owner_telegram_id": model.owner_telegram_id,
            "path_to_img": model.path_to_img,
            "INN": model.INN,
            "balance": model.balance,
            "date": model.date,
            "time": model.time
        }

    def from_document(self, data: dict) -> Check:
        model = Check()
        model.path_to_img = data.get("path_to_img")
        model.INN = data.get("INN")
        model.balance = data.get("balance")
        model.date = data.get("date")
        model.time = data.get("time")
        return model
