import uuid

from core.exceptions import DatabaseException
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from users.enums import RoleEnum
from users.models import User
from users.schemas import CreateUserFullData, RegisterUser
from users.schemas import UpdateUser


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
    async def register_user(new_user: RegisterUser, db: AsyncSession):
        query = insert(User).values(**new_user.dict(), role=RoleEnum.developer).returning(User)
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
    async def get_user_by_email(db: AsyncSession, email: str):
        try:
            query = select(User).where(User.email == email)
            user = await db.execute(query)
            return user.scalar()
        except Exception as e:
            print('123123123')
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

    @staticmethod
    async def soft_delete(user_id: uuid.UUID, db: AsyncSession):
        try:
            query = (
                update(User)
                .where(User.user_id == user_id, User.is_active == True)
                .values(is_active=False)
                .returning(User)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated

        except Exception:
            raise DatabaseException
