from os import stat
from .model import Model


class Check(Model):
    def __init__(self) -> None:
        self.telegram_id = None
        self.owner_telegram_id = None
        self.path_to_img: str = None
        self.INN: str = None
        self.balance: int = None
        self.date: str = None
        self.time: str = None

    @staticmethod
    def from_request(self, args) -> "Check":
        model = Check()
        model.owner_telegram_id = args.get("telegram_id")
        model.path_to_img = args.get("path_to_img")
