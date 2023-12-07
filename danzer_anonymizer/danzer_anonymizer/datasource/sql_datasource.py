from typing import Optional


class SqlDatasource:
    """
    Datasource loaded from relational database
    """
    def __init__(self,
                 name: str,
                 connection_string: str,
                 id: Optional[str] = None):
        self._name = name
        self._connection_string = connection_string
        self._id = id
