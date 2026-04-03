from typing import Callable, Optional
from sqlalchemy import select

from src.utils import CRUD, CrudFinder, DatabaseConnectionInterface
from src.schemas import UserDTO

from .models import User


class UserRepository(CrudFinder):
    _object_type: object = UserDTO

    def __init__(
        self, connection: DatabaseConnectionInterface, autocommit: bool = True
    ):
        self.autocommit: bool = autocommit
        self._connection = connection.connection

    def __del__(self):
        self._connection.close()

    def save(self):
        self._connection.commit()

    def action(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs) -> object:
            result = func(self, *args, **kwargs)

            if self.autocommit:
                self.save()

            return result

        return wrapper

    def find_by(self, field_name: str, field_value: str) -> Optional[User]:
        return self._connection.execute(
            select(User).where(getattr(User, field_name) == field_value)
        )

    @action
    def create(self, obj: _object_type) -> bool:
        self._connection.add(
            User(
                rights=obj.rights,
                full_name=obj.full_name,
                email=obj.email,
                password=obj.password,
            )
        )
        return True

    def read(self, id: int) -> Optional[_object_type]:
        self._connection.query(User).filter(User.id == id).first()

    @action
    def update(self, id, **kwargs) -> bool:
        user = self.read(id)
        if user is None:
            return False

        for key, value in kwargs:
            if user.hasattr(key):
                setattr(user, key, value)
            else:
                return False
        return True

    @action
    def delete(self, id: int) -> bool:
        self.read(id).delete()
