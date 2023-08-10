import pytest

from data_anonymizer.datasource.connector.file_system_connector import FileSystemConnector


@pytest.fixture()
def create_files_and_instantiate_data_connector(tmp_path):
    file_names = ["file1.csv", "file2.csv", "file3.csv"]
    for file_name in file_names:
        file_path = tmp_path / file_name
        with file_path.open("w") as f:
            f.write("Content for " + file_name)

    return FileSystemConnector(
        name="test-fs-connector",
        datasource_name="test-datasource",
        base_directory=str(tmp_path),
        file_regex="*.csv"
    )


def test_list_files_match_regex(create_files_and_instantiate_data_connector):
    fs_data_connector = create_files_and_instantiate_data_connector
    csv_files = fs_data_connector.list_files_match_regex()
    assert len(csv_files) == 3
