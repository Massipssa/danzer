from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class DataSourceDefinition:
    """Pure datasource description independent from concrete connectors."""

    name: str
    config: dict[str, Any] = field(default_factory=dict)
    id: str | None = None
