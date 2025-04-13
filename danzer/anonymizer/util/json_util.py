import json

from danzer.anonymizer.exceptions.exceptions import ConfigLoadError


def load_config_from_json(file_path: str):  # -> AnonymizerConfig:
    """
    Load Anonymizer Configuration from JSON file

    :param file_path: File's path containing the configuration
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError as e:
        raise ConfigLoadError(f"Configuration file '{file_path}' not found.") from e
    except json.JSONDecodeError as e:
        raise ConfigLoadError(f"Error decoding JSON in '{file_path}': {e}") from e
