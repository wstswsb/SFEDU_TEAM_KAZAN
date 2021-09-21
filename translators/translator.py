from abc import (
    ABC,
    abstractmethod,
)
from models import Model


class Translator:
    @abstractmethod
    def from_document(self, data: dict) -> Model: ...
    @abstractmethod
    def to_document(self, model: Model) -> dict: ...
