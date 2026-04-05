from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AnonymizationJobConfig:
    """Normalized configuration consumed by application services."""

    source_path: str
    rule_name: str
    rule_params: dict[str, Any] = field(default_factory=dict)
    engine: str = "spark"
    output_path: str | None = None
