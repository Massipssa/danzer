from dataclasses import dataclass


@dataclass(slots=True)
class LocalFileSource:
    path: str
