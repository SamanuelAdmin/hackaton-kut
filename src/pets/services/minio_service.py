from abc import ABC, abstractmethod
from typing import BinaryIO
from minio import Minio
from uuid import uuid4

from src.pets.services.file_validator import ImageValidatorService
from src.configs import settings

import magic


class IMinioService(ABC):
    @abstractmethod
    def upload(self, file_buffer: BinaryIO, filename: str | None, size: int) -> str:
        """
        Валидирует файл и загружает в хранилище
        Возвращает имя файла в хранилище
        """
        pass

    @abstractmethod
    def remove(self, filename: str) -> None:
        """
        Удаляет файл по указанному имени из хранилища
        """
        pass


class MinioService(IMinioService):
    """
    Класс по работе с Minio хранилищем
    Умеет:
    Добавлять файлы
    Удалять файлы

    Не получает файлы так как этим занимается nginx

    При инцииализации получает на вход валидатор файлов и клиент Minio
    """

    def __init__(
        self, minio_client: Minio, file_validator: ImageValidatorService
    ) -> None:
        self._client = minio_client
        self._file_validator = file_validator

    def _get_file_type(self, _file: BinaryIO) -> str:
        _file.seek(0)
        mime = magic.Magic(mime=True)
        mime_type: str = mime.from_buffer(_file.read(2048))
        _file.seek(0)
        return mime_type.split("/")[-1]

    def upload(self, file_buffer: BinaryIO, filename: str | None, size: int) -> str:
        file_buffer.seek(0)

        self._file_validator.validate_file(
            filename=None, file_content_type=None, _file=file_buffer
        )

        file_buffer.seek(0)

        filetype = self._get_file_type(file_buffer)
        filename = str(uuid4()) + "." + filetype

        if not self._client.bucket_exists(settings.minio.minio_bucket_name):
            self._client.make_bucket(settings.minio.minio_bucket_name)

        self._client.put_object(
            settings.minio.minio_bucket_name, filename, file_buffer, size, filetype
        )
        return filename

    def remove(self, filename: str) -> None:
        if not self._client.bucket_exists(settings.minio.minio_bucket_name):
            self._client.make_bucket(settings.minio.minio_bucket_name)

        self._client.remove_object(settings.minio.minio_bucket_name, filename)
