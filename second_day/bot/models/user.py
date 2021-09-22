

class User:
    def __init__(self) -> None:
        self.id: str = None
        self.fio: str = None

    def assign_request(self, data: dict) -> None:
        self.id = data.get("id")
        self.fio = data.get("fio")

    @staticmethod
    def from_request(data: dict) -> "User":
        user = User()
        user.assign_request(data)
        return user
