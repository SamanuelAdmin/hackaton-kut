from src.schemas import JWTBody, JWTHeader, UserDTO
from src.utils import CRUD


class JWTService:
    def __init__(self, secret: str, default_ttl: int = 3600, algorithm: str = "SHA256"):
        self._secret = secret
        self.default_ttl = default_ttl

    def generate(user: UserDTO) -> str:
        pass


class UserService:
    _object_type = UserDTO

    def __init__(self, database_repository):
        self.database_repository = database_repository

    def create(self, obj: _object_type) -> bool: ...

    def read(self, obj: _object_type) -> bool: ...

    def update(self, obj: _object_type) -> bool: ...

    def delete(self, obj: _object_type) -> bool: ...
