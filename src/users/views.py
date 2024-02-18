import uuid
from typing import List

from auth.services import AuthService
from core.db import get_db
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from users.schemas import CreateUserFullData, RegisterUser
from users.schemas import ShowUser
from users.schemas import UpdateUser
from users.services import UserService

user_router = APIRouter()


@user_router.get("/get_all", response_model=List[ShowUser])
async def get_all_users(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return await UserService.get_all_users_service(db=db, current_user=current_user)


@user_router.get("/get_by_id/{user_id}", response_model=ShowUser)
async def get_user_by_id(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return await UserService.get_user_by_id(
        user_id=user_id, db=db, current_user=current_user
    )


@user_router.get("/get_by_email/{email}", response_model=ShowUser)
async def get_user_by_email(
    email: str,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return await UserService.get_user_by_email(
        email=email, db=db, current_user=current_user
    )


@user_router.delete("/delete/{user_id}")
async def delete_user_by_id(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return await UserService.delete_user_by_id(
        user_id=user_id, db=db, current_user=current_user
    )


@user_router.patch("/update/{user_id}")
async def update_user_by_id(
    user_id: uuid.UUID,
    user: UpdateUser,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return await UserService.update_user_by_id(
        user_id=user_id, user_to_update=user, db=db, current_user=current_user
    )


@user_router.patch("/soft_delete/{user_id}")
async def soft_delete(
    user_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    return await UserService.soft_delete_user(
        user_id=user_id, db=db, current_user=current_user
    )


@user_router.post("/create")
async def create_user_full_data(new_user: CreateUserFullData,
                                db: AsyncSession = Depends(get_db),
                                current_user: User = Depends(AuthService.get_current_user_from_token),):
    return await UserService.create_user(new_user=new_user, db=db, current_user=current_user)


