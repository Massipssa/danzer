from dataclasses import dataclass

from danzer.anonymizer.domain.rules.base import AnonymizationRule


@dataclass(slots=True)
class AnonymizationJob:
    source: object
    rule: AnonymizationRule
    engine_name: str
    output_path: str | None = None
