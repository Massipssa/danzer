from typing import Optional


class PseudoAnonymization:
    def __init__(self, algorithm_name: str, id: Optional[str] = None):
        self._algorithm_name = algorithm_name
        self._id = id

    def pseudo_anonymize(self):
        raise NotImplementedError
