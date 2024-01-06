from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.users.models import Users


class UserDBController:
    @staticmethod
    async def get_users(db: AsyncSession):
        users = await db.execute(select(Users))
        return users.scalars().all()
