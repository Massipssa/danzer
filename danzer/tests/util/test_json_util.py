"""
import json
import pytest

from danzer_anonymizer.anonymizer.exceptions.exceptions import ConfigLoadError
from danzer_anonymizer.anonymizer.util.json_util import load_config_from_json

SAMPLE_CONFIG = {
    {
        "name": "test",
        "operation": {
            "name": "anonymization",
            "algorith_name": "hashing",
            "colum_list": [
                "col1", "col2", "col4"
            ]
        },
        "data_source": {
            "type": "s3",
            "bucket": "",
            "path": ""
        },
        "execution_engine": {
            "name": "SparkEngine"
        }
    }
}


@pytest.fixture
def sample_config_file(tmp_path):
    file_path = tmp_path / "sample_config.json"
    with open(file_path, 'w') as f:
        json.dump(SAMPLE_CONFIG, f)
    return file_path


def test_load_config_from_json_valid(sample_config_file):
    config = load_config_from_json(sample_config_file)
    assert config == SAMPLE_CONFIG


def test_load_config_from_json_file_not_found():
    with pytest.raises(ConfigLoadError):
        load_config_from_json("non_existent_file.json")


def test_load_config_from_json_invalid_json(tmp_path):
    file_path = tmp_path / "invalid_config.json"
    with open(file_path, 'w') as f:
        f.write("this is not a valid JSON")
    with pytest.raises(ConfigLoadError):
        load_config_from_json(file_path)
"""