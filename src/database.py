from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .utils import Singleton, DatabaseConnectionInterface
from .exceptions import *


class DatabaseConnection(DatabaseConnectionInterface, Singleton):
    def __init__(self, host: str, port: int, user: str, password: str):
        self._user = user
        self._password = password
        self.host = host
        self.port = port

        try:
            self._engine = create_engine(
                f"postgresql://{user}:{password}@{host}:{port}"
            )
            Session = sessionmaker(bind=self._engine)
            self._session = Session()
        except Exception as ex:
            print(ex)
            raise DatabaseUnableToConnect()

    @property
    def engine(self):
        return self._engine

    @property
    def connection(self):
        return self._session
