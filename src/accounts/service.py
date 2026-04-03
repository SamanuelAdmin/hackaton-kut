import base64
import datetime
import json

from src.accounts.exceptions import IncorrectPassword, UserNotFound
from src.accounts.configs import password_hash_alg, jwt_hash_alg
from src.accounts.repository import UserRepository
from src.schemas import JWTToken, UserDTO, UserRights, RegistrationDTO, AuthDTO
from src.utils import CrudFinder

from src.database import DatabaseConnection

_database_connection = DatabaseConnection()


class JWTService:
    def __init__(self, secret: str, algorithm, default_ttl: int = 3600):
        self._secret = secret
        self._default_ttl = default_ttl
        self._algorithm = algorithm

    def token_to_string(token: JWTToken) -> str:
        header: str = base64.b64encode(json.dumps({"alg": token.alg}))
        body: str = base64.b64encode(
            json.dumps(
                {
                    "user_id": token.user_id,
                    "user_rights": token.user_rights,
                    "ttl": token.ttl,
                    "creation_time": token.creation_time,
                }
            )
        )

        signature: str = hmac.new(
            self._secret, f"{header}.{body}", self._algorithm
        ).hexdigest()

        return f"{header}.{body}.{signature}"

    def generate(self, user: UserDTO) -> JWTToken:
        return JWTToken(
            user_id=user.id,
            user_rights=user.user_rights,
            ttl=self._default_ttl,
            creation_time=datetime.datetime.now().timestamp(),
        )


class HashedPassword:
    def __init__(self, password: str, algorithm=password_hash_alg):
        self._hasher = hashlib.new(algorithm)
        self._hasher.update(self.hasher.encode())
        self._password: str = self.hasher.hexdigest()

    def __eq__(self, value):
        return self._password == str(value)

    def __str__(self):
        return self._password


class UserService:
    def __init__(self, jwt_secret: str):
        self._jwt_service = JWTService(jwt_secret, jwt_hash_alg)
        self._repository: CrudFinder = UserRepository()

    def create(self, creds: RegistrationDTO) -> JWTToken:
        user = UserDTO(
            rights=UserRights(),
            full_name=creds.full_name,
            email=creds.email,
            password=HashedPassword(creds.clear_password),
        )

        result: bool = self._repository.create(user)

        jwt_token: JWTToken = self._jwt_service.generate(user)
        jwt_token.token = self._jwt_service.token_to_string(jwt_token)

        return jwt_token

    def auth(self, creds: AuthDTO) -> JWTToken:
        user = self._repository.find_by(self, "email", creds.email)
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
