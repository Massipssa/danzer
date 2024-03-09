class DataAnonymizerError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(message)


class ConfigLoadError(DataAnonymizerError):
    """Custom exception for configuration loading errors."""
    pass
