from bson import ObjectId


class Check:
    def __init__(self) -> None:
        self.id: ObjectId = None
        self.owner_id: ObjectId = None
        self.sum: int = None
        self.date: int = None
