from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.users.db_controller import UserDBController
from src.backend.core.db import get_db


class UserService:
    @staticmethod
    async def get_all_users_service(db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_all_users(db)
