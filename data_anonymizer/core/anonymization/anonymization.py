from typing import Optional


class Anonymization:
    def __init__(self, algorithm_name: str, id: Optional[str] = None):
        self._algorithm_name = algorithm_name
        self._id = id

    def anonymize(self):
        raise NotImplementedError
