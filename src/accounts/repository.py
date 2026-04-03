from typing import Callable
from src.utils import CRUD, DatabaseConnectionInterface
from src.schemas import UserDTO
from .models import User

class UserRepository(CRUD):
    _object_type: object = UserDTO

    def __init__(
            self, connection: DatabaseConnectionInterface, autocommit: bool=True
    ):
        self.autocommit: bool = autocommit
        self._connection = connection.connection

    def __del__(self):
        self._connection.close()

    def action(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs) -> object:
            result = func(self, *args, **kwargs)
            
            if self.autocommit:
                self._connection.commit()

            return result
        return wrapper

    @action
    def create(self, obj: _object_type) -> bool: 
        self._connection.add(
            User(
                rights: obj.rights
                full_name: obj.full_name,
                email: obj.email,
                password: obj.password
            ) 
        )


    @action
    def read(self, id: int) -> Optional[_object_type]: 

    @action
    def update(self, obj: _object_type) -> bool: ...

    @action
    def delete(self, id: int) -> bool: ...
