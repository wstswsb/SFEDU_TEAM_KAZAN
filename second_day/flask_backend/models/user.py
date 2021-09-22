from bson import ObjectId

class User:
    def __init__(self) -> None:
        self.id: ObjectId = None
        self.fio: str = None
    