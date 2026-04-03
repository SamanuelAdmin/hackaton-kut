from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .utils import Singleton, DatabaseConnectionInterface
from .exceptions import *


class DatabaseConnection(DatabaseConnectionInterface, Singleton):
    def init(self, host: str, port: int, user: str, password: str):
        self._user = user
        self._password = password
        self.host = host
        self.port = port

        try:
            self._engine = create_engine(
                f"postgresql://{user}:{password}@{host}:{port}"
            )
        except Exception as ex:
            print(ex)
            raise DatabaseUnableToConnect()

        self._init = True

    @property
    def engine(self):
        return self._engine

    @property
    def connection(self):
        if not hasattr(self, "_init"):
            raise NotInitialized()

        Session = sessionmaker(bind=self._engine)
        self._session = Session()
        return self._session
