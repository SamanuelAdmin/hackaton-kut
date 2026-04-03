from enum import EnumMeta
from abc import ABC


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


class CRUD(ABC):
    _object_type: object = object

    def create(self, obj: _object_type) -> bool: ...

    def read(self, obj: _object_type) -> bool: ...

    def update(self, obj: _object_type) -> bool: ...

    def delete(self, obj: _object_type) -> bool: ...
