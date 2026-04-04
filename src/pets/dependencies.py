from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session

from configs import settings
from .service import JWTService
from schemas import JWTToken
from .repository import PetRepository

SessionDep = Annotated[AsyncSession, Depends(get_session)]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="accounts/auth")


def get_pet_repo(session: SessionDep) -> PetRepository:
    return PetRepository(session)


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(token: str = Depends(oauth2_scheme)):
    jwt_service = JWTService(settings.jwt.secret, settings.jwt.alg)
    try:
        jwt_token: JWTToken = jwt_service.token_to_jwt(token)
    except:
        raise credentials_exception

    return jwt_token


PetRepoDap = Annotated[PetRepository, Depends(get_pet_repo)]
