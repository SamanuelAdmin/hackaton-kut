from typing import AsyncGenerator

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from configs import settings

# MODELS
# WARN: if remove this imports then all crashed and tables will not create
from src.pets import  Pet


db = settings.db
async_mysql_url = f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"
sync_mysql_url = f"postgresql+psycopg2://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"

async_engine = create_async_engine(async_mysql_url, echo=True)
sync_engine = create_engine(sync_mysql_url, echo=True)

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