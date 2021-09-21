from .model import Model


class Check(Model):
    def __init__(self) -> None:
        self.path_to_img: str = None
        self.INN: str = None
        self.balance: int = None
        self.date: str = None
        self.time: str = None

    @staticmethod
    def from_request(args: dict) -> "Check":
        check = Check()
        check.path_to_img = args.get("path_to_img")
        return check
