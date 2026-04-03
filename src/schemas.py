from pydantic import BaseModel, Field
from enum import Enum

from src.utils import DefaultEnumMeta


class UserRights(str, Enum, metaclass=DefaultEnumMeta):
    USER = "user"
    ADMIN = "admin"

    def __init__(self):
        return UserRights.USER


class JWTHeader(BaseModel):
    alg: str
    token_type: str


class JWTBody(BaseModel):
    user_id: int
    user_rights: str
    ttl: int

    class Config:
        title = "UserJST"


class UserDTO(BaseModel):
    id: int
    rights: UserRights
    full_name: str
    email: str
    password: str
