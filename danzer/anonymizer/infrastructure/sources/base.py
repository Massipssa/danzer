from typing import Optional

from danzer.anonymizer.datasource.connector.connector_factory import DataConnectorFactory


class DataSource:
    def __init__(self,
                 name: str,
                 config: dict,
                 id: Optional[str] = None):
        self._name = name
        self.config = config
        self.connector = DataConnectorFactory.create(config)
        self._id = id

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> Optional[str]:
        return self._id
