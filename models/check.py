from os import stat
from .model import Model


class Check(Model):
    def __init__(self) -> None:
        self.telegram_img_id = None
        self.telegram_owner_id = None
        self.path_to_img: str = None
        self.INN: str = None
        self.balance: int = None
        self.text: str = None

    @staticmethod
    def from_request(args) -> "Check":
        model = Check()
        model.telegram_owner_id = args.get("telegram_owner_id")
        model.telegram_img_id = args.get("telegram_img_id")
        return
