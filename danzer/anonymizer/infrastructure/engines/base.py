from abc import ABC, abstractmethod

from danzer.anonymizer.domain.rules.base import AnonymizationRule
from danzer.anonymizer.infrastructure.connectors.filesystem import LocalFileSource


class TabularExecutionEngine(ABC):
    @abstractmethod
    def read(self, source: LocalFileSource):
        raise NotImplementedError

    @abstractmethod
    def apply_rule(self, dataset, rule: AnonymizationRule):
        raise NotImplementedError

    @abstractmethod
    def write(self, dataset, output_path: str) -> None:
        raise NotImplementedError
