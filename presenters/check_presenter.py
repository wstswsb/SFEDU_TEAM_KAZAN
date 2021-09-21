from models import Check


class CheckPresenter:
    def to_json(self, check: Check) -> dict:
        return {
            "telegram_owner_id": check.telegram_owner_id,
            "telegram_img_id": check.telegram_img_id,
            "text": check.text,
            "info": {
                "balance": check.balance,
                "int_balance": check.int_balance,
                "INN": check.INN,
                "man_date": check.man_date,
                "man_time": check.man_time,
            }
        }
