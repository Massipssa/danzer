import pytest

from danzer_anonymizer.danzer_anonymizer.config import load_column_suppression


@pytest.fixture
def create_column_suppression_props():
    return {
        "name": "test_data_source",
        "action": "anonymization",
        "algorithm_name": "suppression",
        "data_connector": {
            "name": "FileSystemConnector",
            "base_directory": "data",
            "regex_name": "*.csv"
        },
        "columns": [
            "name",
            "landmark"
        ],
        "engine": "local"
    }


def test_load_column_suppression(create_column_suppression_props):
    column_suppression = load_column_suppression(create_column_suppression_props)
    assert column_suppression.algorithm_name == "suppression"
    assert column_suppression.columns_to_delete == ["name", "landmark"]
