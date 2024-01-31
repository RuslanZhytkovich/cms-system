from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from src.backend.core.exceptions import DatabaseConnectionException
from src.backend.core.settings import DB_URL


try:
    engine = create_async_engine(DB_URL, future=True, echo=True)
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
