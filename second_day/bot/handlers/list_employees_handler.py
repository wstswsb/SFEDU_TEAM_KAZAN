from abc import (
    ABC,
    abstractmethod
)
from telebot import types


class ListEmployeesRequesterInterface(ABC):
    @abstractmethod
    def fetch_users(self, admin_tg_id: str) -> list[dict]: ...


class EmployeeButtonText:
    pass


class ListEmployeesHandler:
    def __init__(self,
                 list_employees_requester: ListEmployeesRequesterInterface
                 ) -> None:
        self.requester = list_employees_requester

    def create_keyboard(self):

        keyboard = types.InlineKeyboardButton()
