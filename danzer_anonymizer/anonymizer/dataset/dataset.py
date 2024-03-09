from danzer_anonymizer.anonymizer.core.engine.execution_engine import ExecutionEngine
from danzer_anonymizer.anonymizer.datasource.connector.data_connector import DataConnector


class Dataset:
    """
    A dataset is responsible ......
    """

    def __init__(self, name: str, data_connector: DataConnector, execution_engine: ExecutionEngine):
        self._name = name
        self._data_connector = data_connector
        self._execution_engine = execution_engine

    @property
    def data_connector(self) -> DataConnector:
        return self._data_connector

    @property
    def execution_engine(self) -> ExecutionEngine:
        return self._execution_engine

    def read(self):
        pass

    def save(self):
        pass
