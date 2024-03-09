from abc import ABC
from enum import Enum
from typing import Optional


class EngineType(Enum):
    IN_MEMORY = 0
    SPARK = 1


class ExecutionEngine(ABC):
    """Handles the logic of anonymization or pseudo-anonymization over the data"""

    def __init__(self,
                 name: Optional[str] = None) -> None:
        self.name = name
        self._config = {
            "name": self.name,
            "module_name": self.__class__.__module__,
            "class_name": self.__class__.__name__,
        }
