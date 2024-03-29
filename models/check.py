from datetime import datetime
from .model import Model


class Check(Model):
    def __init__(self) -> None:
        self.telegram_img_id = None
        self.telegram_owner_id = None
        self.path_to_img: str = None
        self.INN: str = None
        self.balance: str = None
        self.text: str = None
        self.date_of_creation: str = None

        self.man_date: str = None
        self.man_time: str = None
        self.int_balance: int = 0

    def _cut_balance(self, keywords=None) -> None:
        if keywords is None:
            keywords = ["ИТОГО", "СУММА", "ИТОГ"]
        for word in keywords:
            index = self.text.find(word)
            if index != -1:
                self.balance = self.text[index:].replace("\n", "")
                return

    @staticmethod
    def from_request(args) -> "Check":
        model = Check()
        model.telegram_owner_id = args.get("telegram_owner_id")
        model.telegram_img_id = args.get("telegram_img_id")
        return

    def assign_request(self, args: dict) -> None:
        self.telegram_img_id = args.get("telegram_img_id")
        self.telegram_owner_id = args.get("telegram_owner_id")
        self.path_to_img = args.get("path_to_img")
        self.text = args.get("text")
        self._cut_balance()
        self.text = [line for line in args.get("text").strip().split("\n")
                     if line != ""]
        self.date_of_creation = datetime.now().isoformat()

    def __str__(self) -> str:
        return \
            f"< Check object >\n" \
            f"{self.telegram_img_id = }" \
            f"{self.telegram_owner_id = }" \
            f"{self.path_to_img = }" \
            f"{self.INN = }" \
            f"{self.balance = }" \
            f"{self.man_date = }" \
            f"{self.man_time = }" \
            f"{self.int_balance = }" \
            f"{self.text = }"
