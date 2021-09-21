from .translator import Translator
from models import Check


class CheckTranslator(Translator):
    def to_document(self, model: Check) -> dict:
        return {
            "telegram_owner_id": model.telegram_owner_id,
            "telegram_img_id": model.telegram_img_id,
            "path_to_img": model.path_to_img,
            "INN": model.INN,
            "balance": model.balance,
            "text": model.text,
            "date_of_creation": model.date_of_creation,
            "int_balance": model.int_balance,
            "man_date": model.man_date,
            "man_time": model.man_time
        }

    def from_document(self, data: dict) -> Check:
        model = Check()
        model.telegram_img_id = data.get("telegram_img_id")
        model.telegram_owner_id = data.get("telegram_owner_id")
        model.path_to_img = data.get("path_to_img")
        model.INN = data.get("INN")
        model.balance = data.get("balance")
        model.text = data.get("text")
        model.date_of_creation = data.get("date_of_creation")
        model.int_balance = data.get("int_balance")
        model.man_time = data.get("man_time")
        model.man_date = data.get("man_date")
        return model
