import uuid

from starlette import status

from core.db import get_db
from core.exceptions import InvalidPermissionsException
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from users.db_controller import UserDBController
from users.enums import RoleEnum
from users.models import User
from users.schemas import CreateUserFullData, RegisterUser
from users.schemas import UpdateUser
from utils.hasher import Hasher
from utils.permissions import Permission, check_admin_manager_permission


class UserService:
    @staticmethod
    @check_admin_manager_permission
    async def get_all_users_service(current_user: User, db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_all_users(db=db)

    @staticmethod
    @check_admin_manager_permission
    async def get_user_by_email(current_user: User, email: str, db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_user_by_email(email=email, db=db)

    @staticmethod
    @check_admin_manager_permission
    async def get_user_by_id(current_user: User, user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
        return await UserDBController.get_user_by_id(user_id=user_id, db=db)

    @staticmethod
    async def delete_user_by_id(current_user: User, user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
        target_user = await UserDBController.get_user_by_id(user_id=user_id)
        if not Permission.check_delete_patch_permissions(current_user=current_user, target_user=target_user):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden."
            )
        return await UserDBController.delete_user_by_id(user_id=user_id, db=db)

    @staticmethod
    async def update_user_by_id(current_user: User, user_id: uuid.UUID, user_to_update: UpdateUser,
                                db: AsyncSession = Depends(get_db)):
        target_user = await UserDBController.get_user_by_id(user_id=user_id, db=db)
        if not Permission.check_delete_patch_permissions(current_user=current_user, target_user=target_user):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden."
            )
        return await UserDBController.update_user_by_id(user_id=user_id, user=user_to_update, db=db)

    @staticmethod
    async def soft_delete_user(current_user: User, user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
        target_user = await UserDBController.get_user_by_id(user_id=user_id, db=db)
        if not Permission.check_delete_patch_permissions(current_user=current_user, target_user=target_user):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden."
            )
        return await UserDBController.soft_delete(user_id=user_id, db=db)

    @staticmethod
    async def create_user(current_user: User, new_user: CreateUserFullData, db: AsyncSession = Depends(get_db)):
        if not Permission.check_admin_permissions(current_user=current_user):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden."
            )
        new_user.password = Hasher.get_password_hash(new_user.password)
        return await UserDBController.create_user(new_user=new_user, db=db)

