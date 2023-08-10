from typing import Optional

from data_anonymizer.core.datasource.connector.data_connector import DataConnector


class FileSystemConnector(DataConnector):
    """
    A class to define a connector to file system
    """

    def __init__(self,
                 name: str,
                 datasource_name: str,
                 base_directory: str,
                 id: Optional[str] = None
                 ):
        super().__init__(
            name=name,
            id=id,
            datasource_name=datasource_name,
        )
        self.base_directory = base_directory

    def list_files_match_regex(self):
        raise NotImplementedError
