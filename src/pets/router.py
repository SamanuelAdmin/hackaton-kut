from fastapi import APIRouter, HTTPException, Depends, Body, UploadFile

from src.pets.dependencies import (
    PetRepoDap,
    get_current_user,
    credentials_exception,
    PetServiceDap,
)
from src.schemas import AllPetsModel, CreatePetModel, JWTToken, ReadPetModel

from src.pets.enums import AnimalGender, AnimalStatus, AnimalTag

router = APIRouter(prefix="/pets", tags=["pets"])


@router.get("/health", response_model=None)
async def health():
    return {"status": "ok"}


@router.get("/{pet_id}", response_model=ReadPetModel)
async def get_pet(pet_id: int, pet_repo: PetRepoDap):
    pet = await pet_repo.get_by_id(pet_id)
    return pet


@router.post("/get_all", response_model=AllPetsModel)
async def get_all(
    pet_repo: PetRepoDap,
    offset: int = Body(0),
    limit: int = Body(10),
    gender: AnimalGender | None = Body(default=None),
    status: AnimalStatus | None = Body(default=None),
    tags: list[AnimalTag] | None = Body(default=None),
    min_age: int = Body(0),
    max_age: int = Body(3),
):
    pets, count = await pet_repo.get_all(
        offset,
        limit,
        tag_filters=tags,
        min_age=min_age,
        max_age=max_age,
        gender=gender,
        status=status,
    )
    return {"pets": pets, "count": count}


@router.post("", response_model=ReadPetModel)
async def create_pet(
    pet: CreatePetModel,
    pet_repo: PetRepoDap,
    current_user: JWTToken = Depends(get_current_user),
):
    if current_user.user_rights != "admin":
        raise credentials_exception
    return await pet_repo.create(pet)


@router.post("/image")
async def add_image_to_pet(
    pet_service: PetServiceDap, pet_id: int, image: UploadFile
) -> str:
    if image.size is None:
        raise HTTPException(422, "No size")
    await image.seek(0)
    filename = await pet_service.add_image(
        pet_id, image.file, image.size, image.filename
    )
    return filename


@router.delete("")
async def remove_pet(
    pet_id: int,
    pet_repo: PetRepoDap,
    current_user: JWTToken = Depends(get_current_user),
):
    if current_user.user_rights != "admin":
        raise credentials_exception

    await pet_repo.remove(pet_id)
    return {"status": "ok"}
