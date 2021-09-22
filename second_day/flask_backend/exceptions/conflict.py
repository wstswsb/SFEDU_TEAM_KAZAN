from .base_exception import BaseAppException


class Conflict(BaseAppException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.code = 409
