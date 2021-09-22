from models import User


class UserTranslator:

    def from_document(self, document: dict) -> User:
        user = User()
        user.fio = document.get("fio")
        user.id = document.get("_id")
        return user

    def to_document(self, model: User) -> dict:
        return {
            "fio": model.fio
        }
