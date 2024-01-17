from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


from src.backend.auth.hashing import Hasher
from src.backend.core.exceptions import DatabaseException
from src.backend.users.schemas import UserCreateRequest
from src.backend.users.models import User


class UserDBController:
    @staticmethod
    async def get_all_users(db: AsyncSession):
        users = await db.execute(select(User))
        return users.scalars().all()

    @staticmethod
    async def create_user(new_user: UserCreateRequest, db: AsyncSession):
        try:
            query = insert(User).values(**new_user.dict()).returning(User)
            result = await db.execute(query)
            new_user = result.scalar()
            await db.commit()
            return new_user
        except Exception:
            raise DatabaseException
