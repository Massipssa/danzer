from dataclasses import dataclass, field

from danzer.anonymizer.domain.rules.base import AnonymizationRule


@dataclass(slots=True)
class ColumnSuppressionRule(AnonymizationRule):
    columns: list[str] = field(default_factory=list)

    def validate(self) -> None:
        if not self.columns:
            raise ValueError("ColumnSuppressionRule requires at least one column.")
