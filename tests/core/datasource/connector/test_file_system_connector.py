import os

import pytest

from data_anonymizer.datasource.connector.file_system_connector import FileSystemConnector


@pytest.fixture()
def create_files_and_instantiate_data_connector(tmp_path):
    #base_directory = "base_dir_fs"

    file_names = ["file1.csv", "file2.csv", "file3.csv"]
    for file_name in file_names:
        file_path = tmp_path / file_name
        with file_path.open("w") as f:
            f.write("Content for " + file_name)

    return FileSystemConnector(
        name="test-fs-connector",
        datasource_name="test-datasource",
        base_directory=tmp_path.name,
        file_regex="*.csv"
    )


def test_list_files_in_base_directory(tmp_path):
    # Create some files in the temporary directory
    file_names = ["file1.csv", "file2.csv", "file3.csv"]
    for file_name in file_names:
        file_path = tmp_path / file_name
        with file_path.open("w") as f:
            f.write("Content for " + file_name)

    # List files in the temporary directory
    base_files = os.listdir(tmp_path)

    assert len(base_files) == len(file_names), "Number of files should match"
    assert all(file_name in base_files for file_name in file_names), "All files should be present"


def test_list_files_match_regex(create_files_and_instantiate_data_connector):
    fs_data_connector = create_files_and_instantiate_data_connector
    csv_files = fs_data_connector.list_files_match_regex()
    assert len(csv_files) == 3
