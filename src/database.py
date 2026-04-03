from typing import Optional
from sqlalchemy import create_engine

from .utils import Singleton
from .exceptions import *


class DatabaseConnection(Singleton):
    def __init__(self, host: str, port: int, user: str, password: str):
        self._user = user
        self._password = password
        self.host = host
        self.port = port

        try:
            self._connection = create_engine(
                f"postgresql://{user}:{password}@{host}:{port}"
            )
        except Exception as ex:
            raise DatabaseUnableToConnect()

    @property
    def connection(self):
        return self._connection
