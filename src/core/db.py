from core.exceptions import DatabaseConnectionException
from core.settings import SETTINGS
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

try:
    engine = create_async_engine(SETTINGS.DB_URL, future=True, echo=True)
    async_session = async_sessionmaker(engine, expire_on_commit=False)
except Exception:
    raise DatabaseConnectionException


async def get_db() -> AsyncSession:
    try:
        async with async_session() as session:
            yield session
    finally:
        await session.close()


class Base(DeclarativeBase):
    pass
