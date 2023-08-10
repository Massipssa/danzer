from typing import Optional


class Datasource:
    def __init__(self,
                 name: str,
                 id: Optional[str] = None):
        self._name = name
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> Optional[str]:
        return self._id
