import uuid

from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.exceptions import DatabaseException
from src.users.schemas import CreateUserFullData, UpdateUser
from src.users.models import User


class UserDBController:
    @staticmethod
    async def get_all_users(db: AsyncSession):
        users = await db.execute(select(User))
        return users.scalars().all()

    @staticmethod
    async def create_user(new_user: CreateUserFullData, db: AsyncSession):
        query = insert(User).values(**new_user.dict()).returning(User)
        result = await db.execute(query)
        new_user = result.scalar()
        await db.commit()
        return new_user


    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: uuid.UUID):
        try:
            query = select(User).where(User.user_id == user_id)
            user = await db.execute(query)
            return user.scalar()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def delete_user_by_id(db: AsyncSession, user_id: uuid.UUID):
        try:
            query = delete(User).where(User.user_id == user_id)
            await db.execute(query)
            await db.commit()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_user_by_id(user_id: uuid.UUID, user: UpdateUser, db: AsyncSession):
        try:
            query = (
                update(User)
                .where(User.user_id == user_id)
                .values(**user.dict(exclude_none=True))
                .returning(User)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated
        except Exception as e:
            raise DatabaseException(str(e))
