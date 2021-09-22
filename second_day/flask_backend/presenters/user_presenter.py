from models import User


class UserPresenter:
    def to_json(self, model: User) -> dict:
        return {
            "id": str(model.id),
            "fio": model.fio
        }
