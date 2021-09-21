from models import Check


class CheckPresenter:
    def to_json(self, check: Check) -> dict:
        return {
            "telegram_owner_id": check.telegram_owner_id,
            "telegram_img_id": check.telegram_img_id,
            "text": check.text,
            "info": {
                "balance": check.balance,
                "INN": check.INN
            }
        }
