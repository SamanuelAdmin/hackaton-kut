from datetime import datetime

from fastapi import Form
from pydantic import BaseModel, Field

from src.pets.enums import AnimalGender, AnimalStatus, AnimalTag, AnimalType

from configs import settings


class JWTToken(BaseModel):
    alg: str = Field(default=settings.jwt.alg)
    user_id: int
    user_rights: str
    ttl: int
    creation_time: int
    token: str = Field(default="")


class CreatePetModel(BaseModel):
    name: str = Field(max_length=32)
    type: AnimalType
    gender: AnimalGender
    age: int
    description: str
    status: AnimalStatus
    tags: list[AnimalTag]


class CreatePetForm(BaseModel):
    name: str = Form(max_length=32)
    type: AnimalType = Form()
    gender: AnimalGender = Form()
    age: int = Form()
    description: str = Form()
    status: AnimalStatus = Form()
    tags: list[AnimalTag] = Form()


class ReadPetModel(CreatePetModel):
    id: int

    image: str | None

    created_at: datetime | None = None
    updated_at: datetime | None = None


class UpdatePetModel(BaseModel):
    name: str | None = None
    type: AnimalType | None = None
    gender: AnimalGender | None = None
    age: int | None = None
    description: str | None = None
    status: AnimalStatus | None = None
    tags: list[AnimalTag] | None = None
    image: str | None


class AllPetsModel(BaseModel):
    pets: list[ReadPetModel]
    count: int
