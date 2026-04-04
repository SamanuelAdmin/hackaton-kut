import hmac
from datetime import datetime
import hashlib
import json
import base64

from utils import Singleton
from schemas import JWTToken
from pets.exceptions import (
    ExpiredTokenError,
    InvalidSignature,
    IncorrectTokenStructure,
    IncorrectTokenContent,
)


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


class JWTService(Singleton):
    def __init__(self, secret: str, algorithm: str):
        self._secret = secret
        self._algorithm = getattr(hashlib, algorithm)

    def is_admin(self, jwt_token: JWTToken) -> bool:
        return jwt_token.user_rights == "admin"

    def _check_ttl(self, ttl: int, creation_time: int) -> bool:
        # true - token still alive
        # false - token expired
        current_time: int = int(datetime.now().timestamp())
        return (creation_time + ttl) < current_time

    def token_to_jwt(token: str) -> JWTToken:
        try:
            header, body, signature = map(
                lambda x: base64.urlsafe_b64decode(x), token.split(".")
            )
        except:
            raise IncorrectTokenStructure()

        # checking the signature
        new_signature = b64url(
            hmac.new(
                self._secret, f"{header}.{body}".encode(), self._algorithm
            ).digest()
        )

        if new_signature != signature:
            raise InvalidSignature()

        # parsing json
        try:
            header: dict = json.loads(header)
            body: dict = json.loads(body)

            # parsing useful data
            jwt_token = JWTToken(
                user_id=body["user_id"],
                user_rights=body["user_rights"],
                ttl=body["ttl"],
                creation_time=body["creation_time"],
            )
        except:
            raise IncorrectTokenContent()

        if not self._check_ttl(jwt_token.ttl, jwt_token.creation_time):
            raise ExpiredTokenError()

        return jwt_token
