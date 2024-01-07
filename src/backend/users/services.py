from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.auth.hashing import Hasher
from src.backend.users.models import RoleEnum
from src.backend.users.schemas import UserCreateRequest
from src.backend.users.db_controller import UserDBController
from src.backend.core.db import get_db
from src.backend.users.models import User


class UserService:
    @staticmethod
    async def get_all_users_service(db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_all_users(db)

    @staticmethod
    async def create_user_service(new_user: UserCreateRequest, db: AsyncSession = Depends(get_db)):
        new_user.password = Hasher.get_password_hash(new_user.password)
        new_user.role = RoleEnum.developer

        # Создаем новый экземпляр User с данными из UserCreateRequest
        user_instance = User(**new_user.dict())

        return await UserDBController.create_user(user_instance, db)


