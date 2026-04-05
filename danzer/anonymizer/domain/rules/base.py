from abc import ABC, abstractmethod


class AnonymizationRule(ABC):
    """Pure domain contract for anonymization rules."""

    @abstractmethod
    def validate(self) -> None:
        raise NotImplementedError
