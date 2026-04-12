from functools import lru_cache
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from minio import Minio
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session
from src.configs import settings

from configs import settings
from src.service import JWTService
from schemas import JWTToken
from src.repository import PetRepository
from src.pets.repository import PetRepository
from src.pets.services.file_validator import ImageValidatorService
from src.pets.services.minio_service import MinioService
from src.pets.services.pet_service import PetService

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


@lru_cache()  # кэширует этот объект Minio, типа как singleton токо умнее
def get_minio() -> Minio:
    return Minio(
        settings.minio.endpoint,
        settings.minio.access_key,
        settings.minio.secret_key,
        secure=settings.minio.secure,
    )


MinioDap = Annotated[Minio, Depends(get_minio)]


def get_image_validator() -> ImageValidatorService:
    return ImageValidatorService()


ImageValidatorDap = Annotated[ImageValidatorService, Depends(get_image_validator)]


def get_minio_service(
    minio: MinioDap, file_validator: ImageValidatorDap
) -> MinioService:
    return MinioService(minio, file_validator)


MinioServiceDap = Annotated[MinioService, Depends(get_minio_service)]
PetRepoDap = Annotated[PetRepository, Depends(get_pet_repo)]


def get_pet_service(minio_service: MinioServiceDap, pet_repo: PetRepoDap) -> PetService:
    return PetService(minio_service, pet_repo)


PetServiceDap = Annotated[PetService, Depends(get_pet_service)]
