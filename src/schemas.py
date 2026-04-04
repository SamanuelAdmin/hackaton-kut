from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from .utils import DefaultEnumMeta
from .accounts.configs import jwt_hash_alg


class UserRights(str, Enum, metaclass=DefaultEnumMeta):
    USER = "user"
    ADMIN = "admin"


class JWTToken(BaseModel):
    alg: str = Field(default=jwt_hash_alg)
    user_id: int
    user_rights: str
    ttl: int
    creation_time: int
    token: str = Field(default="")


class UserDTO(BaseModel):
    id: int = Field(default=-1)
    rights: UserRights = Field(default=UserRights())
    full_name: str
    email: str
    password: str  # encrypted


class RegistrationDTO(BaseModel):
    full_name: str
    email: str
    clear_password: str  # plain text password


class AuthDTO(BaseModel):
    email: str
    clear_password: str


class ChangeDTO(BaseModel):
    full_name: str
    password: str
