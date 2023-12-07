class DatabaseConfig:
    def __init__(self,
                 username: str,
                 password: str,
                 host: str,
                 port: int,
                 db_name: str):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    