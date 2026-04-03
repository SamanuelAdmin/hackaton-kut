from src.utils import CRUD
from src.schemas import UserDTO


class UserRepository(CRUD):
    _object_type = UserDTO

    def __init__(self, database_repository):
        self.database_repository = database_repository

    def create(self, obj: _object_type) -> bool: ...

    def read(self, obj: _object_type) -> bool: ...

    def update(self, obj: _object_type) -> bool: ...

    def delete(self, obj: _object_type) -> bool: ...
