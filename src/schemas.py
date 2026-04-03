from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from src.utils import DefaultEnumMeta


class UserRights(str, Enum, metaclass=DefaultEnumMeta):
    USER = "user"
    ADMIN = "admin"


class JWTHeader(BaseModel):
    alg: str
    token_type: str


class JWTBody(BaseModel):
    user_id: int
    user_rights: str
    ttl: int


class UserDTO(BaseModel):
    id: Optional[int]
    rights: Optional[UserRights]
    full_name: str
    email: str
    password: str
