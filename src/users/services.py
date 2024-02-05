import uuid

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.users.schemas import UpdateUser, CreateUserFullData
from src.users.db_controller import UserDBController
from src.core.db import get_db
from src.users.models import User


class UserService:
    @staticmethod
    async def get_all_users_service(db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_all_users(db)

    @staticmethod
    async def get_user_by_id(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_user_by_id(user_id=user_id, db=db)

    @staticmethod
    async def delete_user_by_id(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
        return await UserDBController.delete_user_by_id(user_id=user_id, db=db)

    @staticmethod
    async def update_user_by_id(user_id: uuid.UUID, user: UpdateUser, db: AsyncSession = Depends(get_db)):
        return await UserDBController.update_user_by_id(user_id=user_id, user=user, db=db)

    @staticmethod
    async def create_user(new_user: CreateUserFullData, db: AsyncSession = Depends(get_db)):
        return await UserDBController.create_user(new_user=new_user, db=db)




