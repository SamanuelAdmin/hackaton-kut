from typing import Generic, Sequence, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from pets import Base, Pet
from pets.exceptions import NoEntityByIdFound
from schemas import CreatePetModel, UpdatePetModel

T = TypeVar("T", bound=Base)
P = TypeVar("P", bound=BaseModel)


class BaseRepository(Generic[T, P]):
    model: Type[T]

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, model: P) -> T:
        new = self.model(**model.model_dump())
        self.session.add(new)
        await self.session.flush()
        await self.session.refresh(new)
        return new

    async def create_all(self, models: list[P]) -> list[T]:
        new_models = [self.model(**model.model_dump()) for model in models]
        self.session.add_all(new_models)
        return new_models

    async def get_by_id(self, entity_id: int) -> T:
        res = await self.session.get(self.model, entity_id)
        if res is None:
            raise NoEntityByIdFound
        return res

    async def get_all(
        self, offset: int, limit: int, **filters
    ) -> tuple[Sequence[T], int]:
        stmt = select(self.model)

        stmt_filters = []
        if filters:
            for k, v in filters.items():
                if hasattr(self.model, k) and getattr(self.model, k):
                    stmt_filters.append(getattr(self.model, k) == v)

        stmt = stmt.where(*stmt_filters)
        stmt = stmt.offset(offset).limit(limit)

        res = await self.session.execute(stmt)
        count = await self.session.execute(
            select(func.count()).select_from(self.model).where(*stmt_filters)
        )

        return res.scalars().all(), count.scalar_one()

    async def get_random(self, limit: int, **filters) -> Sequence[T]:
        stmt_filters = []
        if filters:
            for k, v in filters.items():
                if hasattr(self.model, k) and getattr(self.model, k):
                    stmt_filters.append(getattr(self.model, k) == v)

        projects = await self.session.execute(
            select(self.model).where(*stmt_filters).order_by(func.rand()).limit(limit)
        )
        return projects.scalars().all()

    async def remove(self, entity_id: int) -> T:
        obj = await self.get_by_id(entity_id)
        await self.session.delete(obj)
        return obj


class PetRepository(BaseRepository[Pet, CreatePetModel]):
    model = Pet

    async def update(self, entity_id: int, update_model: UpdatePetModel):
        entity = await self.get_by_id(entity_id)
        update_model_dict = update_model.model_dump()
        for k, _ in entity.__dict__.items():
            if (new_v := update_model_dict.get(k)) is not None:
                setattr(entity, k, new_v)

        return entity
