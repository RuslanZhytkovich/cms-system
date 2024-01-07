from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.users.db_controller import UserDBController
from src.backend.core.db import get_db
from src.backend.users.services import UserService
from src.backend.users.schemas import ShowUser, UserCreateRequest

user_router = APIRouter()


@user_router.get("/all", response_model=List[ShowUser])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await UserService.get_all_users_service(db)


@user_router.post('/create_user')
async def create_user(user: UserCreateRequest, db: AsyncSession = Depends(get_db)):
    return await UserDBController.create_user(user, db)
