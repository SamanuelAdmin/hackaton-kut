from datetime import datetime

from pydantic import BaseModel, Field

from pets.enums import AnimalGender, AnimalStatus, AnimalTag, AnimalType


class CreatePetModel(BaseModel):
    name: str = Field(max_length=32)
    type: AnimalType
    gender: AnimalGender
    age: int
    description: str
    status: AnimalStatus
    tags: list[AnimalTag]


class ReadPetModel(BaseModel):
    id: int

    name: str = Field(max_length=32)
    type: AnimalType
    gender: AnimalGender
    age: int
    description: str
    status: AnimalStatus
    tags: list[AnimalTag] = []

    created_at: datetime
    updated_at: datetime


class UpdatePetModel(CreatePetModel):
    pass


class AllPetsModel(BaseModel):
    pets: list[ReadPetModel]
    count: int
