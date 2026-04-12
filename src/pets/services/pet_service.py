from typing import BinaryIO

from src.pets.services.minio_service import IMinioService
from src.pets.repository import PetRepository

from src.pets.models import Pet


class PetService:
    def __init__(self, minio_service: IMinioService, pet_repo: PetRepository) -> None:
        self._minio_service = minio_service
        self._pet_repo = pet_repo

    async def add_image(
        self,
        pet_id: int,
        file_buffer: BinaryIO,
        size: int,
        filename: str | None = None,
    ) -> str:
        pet = await self._pet_repo.get_by_id(pet_id)
        image_filename = self._minio_service.upload(file_buffer, filename, size)
        pet.image = image_filename

        await self._pet_repo.session.commit()
        return image_filename
