class ObjectDataSource:
    """In-memory datasource backed by a Python object."""

    def __init__(self, name: str, payload=None):
        self._name = name
        self.payload = payload
