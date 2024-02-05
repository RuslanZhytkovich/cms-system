
import asyncio

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


from core.db import Base
from core.redis import RedisRepository
from main import app

@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def engine():
    db_url = "postgresql+asyncpg://postgres_test:postgres_test@localhost:5433/postgres_test"
    engine = create_async_engine(db_url)
    yield engine
    engine.sync_engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def create(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        pass
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client(event_loop, create):
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
        yield ac


@pytest_asyncio.fixture
async def session(engine):
    async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session() as session:
        yield session






