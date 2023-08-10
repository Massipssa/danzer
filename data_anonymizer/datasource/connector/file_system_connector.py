import fnmatch
import os

from typing import Optional, List

from data_anonymizer.datasource.connector.data_connector import DataConnector


class FileSystemConnector(DataConnector):
    """
    A class to define a connector to file system
    """

    def __init__(self,
                 name: str,
                 datasource_name: str,
                 base_directory: str,
                 file_regex: str = None,
                 id: Optional[str] = None
                 ):
        super().__init__(
            name=name,
            id=id,
            datasource_name=datasource_name,
        )
        self.base_directory = base_directory
        self.file_regex = file_regex

    def list_files_match_regex(self) -> Optional[List[str]]:
        """
        List all files that match regex from base directory
        """
        return [f for f in os.listdir(self.base_directory) if fnmatch.fnmatch(f, self.file_regex)]
