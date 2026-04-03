from enum import EnumMeta
from abc import ABC, abstractmethod
from typing import Optional


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class DefaultEnumMeta(EnumMeta):
    default = object()

    def __call__(cls, value=default, *args, **kwargs):
        if value is DefaultEnumMeta.default:
            # Assume the first enum is default
            return next(iter(cls))
        return super().__call__(value, *args, **kwargs)


class DatabaseConnectionInterface(ABC):
    @property
    @abstractmethod
    def connection(self): ...

    @property
    @abstractmethod
    def engine(self): ...


class Finder(ABC):
    _object_type: object = object

    def find_by(self, *args, **kwargs) -> _object_type: ...


class CRUD(ABC):
    _object_type: object = object

    @abstractmethod
    def create(self, obj: _object_type) -> int: ...

    @abstractmethod
    def read(self, id: int) -> Optional[_object_type]: ...

    @abstractmethod
    def update(self, obj: _object_type) -> bool: ...

    @abstractmethod
    def delete(self, id: int) -> bool: ...


class CrudFinder(CRUD, Finder):
    pass
