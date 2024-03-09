from danzer_anonymizer.anonymizer.config.data_connector_config import load_fs_data_connector_props


def test_load_fs_data_connector_props():
    json_data_connector = {
        "name": "FileSystemConnector",
        "base_directory": "data/test",
        "regex_name": "*.csv"
    }

    data_connector = load_fs_data_connector_props(json_data_connector)
    assert data_connector.name == "FileSystemConnector"
    assert data_connector.base_directory == "data/test"
    assert data_connector.file_regex == "*.csv"
