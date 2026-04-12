from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.configs import settings


db = settings.db
async_postgres_url = (
    f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"
)
sync_postgres_url = (
    f"postgresql+psycopg2://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"
)

async_engine = create_async_engine(
    async_postgres_url, echo=db.echo, echo_pool=db.echo_pool
)
sync_engine = create_engine(sync_postgres_url, echo=db.echo, echo_pool=db.echo_pool)

AsyncSessionMaker = async_sessionmaker(
    async_engine, expire_on_commit=False, autoflush=False
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionMaker() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
