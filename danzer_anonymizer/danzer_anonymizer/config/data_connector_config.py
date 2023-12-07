from typing import Dict, Any

from danzer_anonymizer.danzer_anonymizer.datasource.connector.file_system_connector import FileSystemConnector


def load_fs_data_connector_props(json_data: Dict[str, Any]) -> FileSystemConnector:
    fs_data_connector = FileSystemConnector(
        name=json_data["name"],
        # todo
        datasource_name=None,  # json_data[""],
        base_directory=json_data["base_directory"],
        file_regex=json_data["regex_name"]
    )
    return fs_data_connector
