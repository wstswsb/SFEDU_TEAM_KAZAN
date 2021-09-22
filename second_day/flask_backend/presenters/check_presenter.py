from models import Check


class CheckPresenter:
    def to_json(self, model: Check) -> dict:
        return {
            "id": str(model.id),
            "sum": model.sum,
            "owner_id": str(model.owner_id),
            "date": model.date
        }