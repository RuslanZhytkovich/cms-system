import uuid
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_db
from users.services import UserService
from users.schemas import ShowUser, CreateUserFullData, UpdateUser

user_router = APIRouter()


@user_router.get("/get_all", response_model=List[ShowUser])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await UserService.get_all_users_service(db=db)


@user_router.get("/get_by_id", response_model=ShowUser)
async def get_user_by_id(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await UserService.get_user_by_id(user_id=user_id, db=db)


@user_router.delete("/delete")
async def delete_user_by_id(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await UserService.delete_user_by_id(user_id=user_id, db=db)


@user_router.patch("/update")
async def update_user_by_id(user_id: uuid.UUID, user: UpdateUser, db: AsyncSession = Depends(get_db)):
    return await UserService.update_user_by_id(user_id=user_id, user=user,db=db)


@user_router.patch("/soft_delete")
async def update_user_by_id(user_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await UserService.soft_delete_user(user_id=user_id,db=db)


@user_router.post('/create')
async def create_user(new_user: CreateUserFullData, db: AsyncSession = Depends(get_db)):
    return await UserService.create_user(new_user=new_user, db=db)
