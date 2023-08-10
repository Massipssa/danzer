from typing import Optional, Dict


class Anonymization:
    ALGORITHM_NAME_TO_ABBREVIATION_NAME_MAP: Dict[str, str] = {
        "ColumnSuppression": "Drop",
        "KAnonymity": "Kanonymity"
    }

    def __init__(self, algorithm_name: str, id: Optional[str] = None):
        self._algorithm_name = algorithm_name
        self._id = id

    def anonymize(self):
        raise NotImplementedError
