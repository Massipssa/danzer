from dataclasses import dataclass


@dataclass(slots=True)
class DatasetDefinition:
    """Pure dataset description used by the application layer."""

    name: str
    source: object
    engine: object
