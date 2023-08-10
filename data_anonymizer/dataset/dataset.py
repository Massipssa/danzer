from data_anonymizer.datasource.connector.data_connector import DataConnector


class Dataset:
    """
    A dataset is responsible for all data loaded from different connectors
    """
    def __init__(self, name: str, data_connector: DataConnector):
        self._name = name
        self._data_connector = data_connector

    def read(self):
        pass

    def save(self):
        pass
