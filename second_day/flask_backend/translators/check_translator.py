from models import Check


class CheckTranslator:
    def from_document(self, document: dict) -> Check:
        check = Check()
        check.id = document.get("_id")
        check.date = document.get("date")
        check.owner_id = document.get("owner_id")
        check.sum = document.get("sum")
        return check

    def to_document(self, model: Check) -> dict:
        return {
            "date": model.date,
            "owner_id": model.owner_id,
            "sum": model.sum
        }
