from fastapi import APIRouter, HTTPException, Depends

from pets.dependencies import PetRepoDap, get_current_user, credentials_exception
from pets.exceptions import NoEntityByIdFound
from schemas import AllPetsModel, CreatePetModel, JWTToken, ReadPetModel
from fastapi import APIRouter

from pets.dependencies import PetRepoDap
from schemas import AllPetsModel, CreatePetModel, ReadPetModel

router = APIRouter(prefix="/pets", tags=["pets"])


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/{pet_id}", response_model=ReadPetModel)
async def get_pet(pet_id: int, pet_repo: PetRepoDap):
    pet = await pet_repo.get_by_id(pet_id)
    return pet


@router.get("", response_model=AllPetsModel)
async def get_all(pet_repo: PetRepoDap, offset: int, limit: int):
    pets, count = await pet_repo.get_all(offset, limit)
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


@router.delete("")
async def remove_pet(
    pet_id: int,
    pet_repo: PetRepoDap,
    current_user: JWTToken = Depends(get_current_user),
):
    if current_user.user_rights != "admin":
        raise credentials_exception

    try:
        await pet_repo.remove(pet_id)
        return {"status": "ok"}
    except NoEntityByIdFound:
        raise HTTPException(404, "Not found pet by id.")


@router.put("")
async def remove_pet(pet_id: int, pet_repo: PetRepoDap):
    await pet_repo.remove(pet_id)
    return {"status": "ok"}
