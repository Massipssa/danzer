import fnmatch
import os

from typing import Optional, List

from danzer.anonymizer.datasource.connector.data_connector import DataConnector


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
        self._base_directory = base_directory
        self._file_regex = file_regex

    @property
    def base_directory(self):
        return self._base_directory

    @property
    def file_regex(self):
        return self._file_regex

    def list_files_match_regex(self) -> Optional[List[str]]:
        """
        List all files that match regex from base directory
        """
        return [f for f in os.listdir(self._base_directory) if fnmatch.fnmatch(f, self._file_regex)]
