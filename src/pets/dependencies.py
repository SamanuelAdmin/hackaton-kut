from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session

from .repository import PetRepository

SessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_pet_repo(session: SessionDep) -> PetRepository:
    return PetRepository(session)


PetRepoDap = Annotated[PetRepository, Depends(get_pet_repo)]
