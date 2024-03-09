from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class ActionType(Enum):
    Anonymize = 1
    Deanonymize = 2


class Action(ABC):
    """Action abstract class to be implemented by each action."""

    @abstractmethod
    def operate(self, params: Dict = None) -> str:
        """Operate method to be implemented in each action."""
        pass

    @abstractmethod
    def validate(self, params: Dict = None) -> None:
        """Validate each action parameters."""
        pass

    @abstractmethod
    def action_name(self) -> str:
        """Return action name."""
        pass

    @abstractmethod
    def action_type(self) -> ActionType:
        """Return operator type."""
        pass


class ActionConfig:

    def __init__(self,
                 name: str,
                 params: dict = None):
        self.name = name
        if not params:
            params = {}
        self.params = params
