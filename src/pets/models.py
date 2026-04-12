from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.pets.enums import AnimalType, AnimalGender, AnimalStatus, AnimalTag


class Base(DeclarativeBase):
    pass


class Pet(Base):
    __tablename__ = "pets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(String(length=32))
    type: Mapped[AnimalType]
    gender: Mapped[AnimalGender]
    age: Mapped[int]
    description: Mapped[str]
    status: Mapped[AnimalStatus]
    tags: Mapped[list[AnimalTag]] = mapped_column(ARRAY(String))
    image: Mapped[str | None] = mapped_column(nullable=True, default=None)

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
