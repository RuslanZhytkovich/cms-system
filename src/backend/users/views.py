from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from src.backend.core.db import get_db
from src.backend.users.db_controller import UserDBController
from src.backend.users.schemas import ShowUser


user_router = APIRouter()


@user_router.get("/all", response_model=List[ShowUser])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    #users_data = [jsonable_encoder(user) for user in users]
    return await UserDBController.get_users(db)