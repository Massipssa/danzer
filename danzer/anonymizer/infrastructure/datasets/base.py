from danzer.anonymizer.datasource.connector.data_connector import DataConnector
from danzer.anonymizer.engine.execution_engine import ExecutionEngine


class Dataset:
    """Infrastructure representation of a dataset bound to IO adapters."""

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
        raise NotImplementedError

    def save(self):
        raise NotImplementedError
