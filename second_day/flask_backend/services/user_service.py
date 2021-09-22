from models import User
from repositories import UserRepository




class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository: UserRepository = repository

    def get_all(self) -> list[User]:
        self.repository.get_all()