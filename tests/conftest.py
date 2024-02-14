import asyncio

import pytest
import pytest_asyncio
from core.base import Base
from core.db import get_db
from core.settings import SETTINGS
from httpx import AsyncClient
from main import app
from sqlalchemy import insert
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from users.enums import RoleEnum
from users.models import User
from utils.hasher import Hasher

engine_test = create_async_engine(SETTINGS.TEST_DB_URL, poolclass=NullPool)
async_session_maker = sessionmaker(
    engine_test, class_=AsyncSession, expire_on_commit=False
)
Base.metadata.bind = engine_test


async def override_get_async_session():
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[get_db] = override_get_async_session


@pytest.fixture(scope="session")
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def engine():
    db_url = (
        "postgresql+asyncpg://postgres_test:postgres_test@localhost:5429/postgres_test"
    )
    engine = create_async_engine(db_url)
    yield engine
    engine.sync_engine.dispose()


@pytest_asyncio.fixture(scope="session")
async def create(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def client(event_loop, create):
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
        # await RedisRepository.connect_to_redis()
        pass

        yield ac


@pytest_asyncio.fixture
async def session(engine):
    async_session = async_sessionmaker(
        bind=engine, expire_on_commit=False, class_=AsyncSession
    )
    async with async_session() as session:
        yield session


@pytest.fixture
async def create_admin(session, client):
    password = Hasher.get_password_hash("admin")
    query = (
        insert(User)
        .values(email="admin@gmail.com", password=password, role=RoleEnum.admin)
        .returning(User)
    )
    await session.execute(query)
    await session.commit()

    payload = {"username": "admin@gmail.com", "password": "admin"}
    response = await client.post("/login/token", json=payload)
    print("11111", response)
    response_data = response.json()
    access_token = response_data["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    return headers
