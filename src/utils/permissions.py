from functools import wraps
from typing import Union

from core.exceptions import InvalidCredentialsException
from core.exceptions import NotFoundException
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from users.db_controller import UserDBController
from users.enums import RoleEnum
from users.models import User
from utils.hasher import Hasher


class Permission:
    @staticmethod
    def check_delete_patch_permissions(current_user: User, target_user: User) -> bool:
        if not current_user.is_active:
            return False
        if (
            target_user.user_id == current_user.user_id
            or target_user.role == RoleEnum.admin
        ):
            return False
        if current_user.role == RoleEnum.manager and target_user.role in (
            RoleEnum.manager,
            RoleEnum.admin,
        ):
            return False
        if current_user.role == RoleEnum.admin and target_user.role == RoleEnum.admin:
            return False
        if current_user.role == RoleEnum.developer:
            return False
        return True

    @staticmethod
    def check_admin_manager_permissions(current_user: User) -> bool:
        if not current_user.is_active:
            return False
        if current_user.role == RoleEnum.developer:
            return False
        return True

    @staticmethod
    def check_admin_permissions(current_user: User) -> bool:
        if not current_user.is_active:
            return False
        if current_user.role != RoleEnum.admin:
            return False
        return True


def check_admin_manager_permission(func):
    @wraps(func)
    async def wrapper(current_user: User, *args, **kwargs):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden."
            )
        return await func(current_user, *args, **kwargs)

    return wrapper


async def authenticate_user(
    email: str, password: str, db: AsyncSession
) -> Union[User, None]:
    user = await UserDBController.get_user_by_email(email=email, db=db)

    if user is None:
        raise NotFoundException

    if not Hasher.verify_password(password, user.password):
        raise InvalidCredentialsException
    return user
