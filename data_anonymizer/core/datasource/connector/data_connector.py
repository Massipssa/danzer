from typing import Optional


class DataConnector:
    """
    A base class for all data connectors
    """

    def __int__(self,
                name: str,
                datasource_name: str,
                id: Optional[str] = None):
        self._name = name
        self._id = id
        self._datasource_name = datasource_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def datasource_name(self) -> str:
        return self._datasource_name

    @property
    def id(self) -> Optional[str]:
        return self._id