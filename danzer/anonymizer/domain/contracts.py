from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Optional


class ActionType(Enum):
    Anonymize = 1
    Deanonymize = 2


class Action(ABC):
    """Legacy-compatible business action contract."""

    @abstractmethod
    def operate(self, params: Optional[Dict] = None):
        raise NotImplementedError

    @abstractmethod
    def validate(self, params: Optional[Dict] = None) -> None:
        raise NotImplementedError

    @abstractmethod
    def action_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def action_type(self) -> ActionType:
        raise NotImplementedError


class Rule(ABC):
    """Legacy-compatible rule contract."""

    def __init__(self, columns: list, params: dict | None = None):
        self.columns = columns
        self.params = params or {}

    @abstractmethod
    def apply(self, params: Dict | None = None):
        raise NotImplementedError

    @abstractmethod
    def validate(self, params: Dict | None = None) -> None:
        raise NotImplementedError

    @abstractmethod
    def action_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def action_type(self) -> ActionType:
        raise NotImplementedError


class ActionConfig:
    def __init__(self, name: str, params: dict | None = None):
        self.name = name
        self.params = params or {}
