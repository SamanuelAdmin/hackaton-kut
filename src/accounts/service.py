import base64
import hmac
from typing import Callable
import hashlib
import datetime
import json

from src.accounts.exceptions import IncorrectPassword, UserNotFound
from src.accounts.configs import password_hash_alg, jwt_hash_alg
from src.accounts.repository import UserRepository
from src.accounts.exceptions import *
from src.schemas import JWTToken, UserDTO, UserRights, RegistrationDTO, AuthDTO
from src.utils import CrudFinder

from src.database import DatabaseConnection


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


class JWTService:
    def __init__(self, secret: str, algorithm, default_ttl: int = 3600):
        self._secret = secret.encode()
        self._default_ttl = default_ttl
        self._algorithm = algorithm

    def token_to_string(self, token: JWTToken) -> str:
        header: str = b64url(json.dumps({"alg": token.alg}).encode())
        body: str = b64url(
            json.dumps(
                {
                    "user_id": token.user_id,
                    "user_rights": token.user_rights,
                    "ttl": token.ttl,
                    "creation_time": token.creation_time,
                }
            ).encode()
        )

        signature: str = b64url(
            hmac.new(
                self._secret, f"{header}.{body}".encode(), self._algorithm
            ).digest()
        )

        return f"{header}.{body}.{signature}"

    def generate(self, user: UserDTO) -> JWTToken:
        return JWTToken(
            user_id=user.id,
            user_rights=user.rights,
            ttl=self._default_ttl,
            creation_time=int(datetime.datetime.now().timestamp()),
        )


class HashedPassword:
    def __init__(self, password: str, algorithm=password_hash_alg):
        self._hasher = hashlib.new(algorithm)
        self._hasher.update(password.encode())
        self._password: str = self._hasher.hexdigest()

    def __eq__(self, value):
        return self._password == str(value)

    def __str__(self):
        return self._password


class UserService:
    def __init__(self, jwt_secret: str):
        self._jwt_service = JWTService(jwt_secret, getattr(hashlib, jwt_hash_alg))

    def add_repository(func: Callable) -> Callable:
        def wrapper(self, *args, **kwargs) -> object:
            session = DatabaseConnection()
            self._repository: CrudFinder = UserRepository(session)

            return func(self, *args, **kwargs)

        return wrapper

    @add_repository
    def create(self, creds: RegistrationDTO) -> JWTToken:
        user = UserDTO(
            rights=UserRights().value,
            full_name=creds.full_name,
            email=creds.email,
            password=str(HashedPassword(creds.clear_password)),
        )
        try:
            user_id: int = self._repository.create(user)
        except:
            raise IncorrectValue()

        user.id = user_id

        jwt_token: JWTToken = self._jwt_service.generate(user)
        jwt_token.token = self._jwt_service.token_to_string(jwt_token)

        return jwt_token

    @add_repository
    def auth(self, creds: AuthDTO) -> JWTToken:
        user = self._repository.find_by("email", creds.email)
        if not user:
            raise UserNotFound()

        if not (HashedPassword(creds.clear_password) == user.password):
            raise IncorrectPassword()

        userDTO = UserDTO(
            id=user.id,
            rights=user.rights,
            full_name=user.full_name,
            email=user.email,
            password=user.password,
        )

        jwt_token: JWTToken = self._jwt_service.generate(userDTO)
        jwt_token.token = self._jwt_service.token_to_string(jwt_token)

        return jwt_token
