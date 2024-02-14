from typing import List

from auth.services import AuthService
from core.db import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from specializations.schemas import CreateSpecialization
from specializations.schemas import ShowSpecialization
from specializations.schemas import UpdateSpecialization
from specializations.services import SpecializationService
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User

specialization_router = APIRouter()


@specialization_router.get("/get_all", response_model=List[ShowSpecialization])
async def get_all_specializations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await SpecializationService.get_all_specializations_service(
            db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.get(
    "/get_by_id/{specialization_id}", response_model=ShowSpecialization
)
async def get_specialization_by_id(
    specialization_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await SpecializationService.get_specialization_by_id(
            specialization_id=specialization_id, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.delete(
    "/delete_by_id/{specialization_id}", status_code=status.HTTP_200_OK
)
async def delete_specialization_by_id(
    specialization_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await SpecializationService.delete_specialization_by_id(
            specialization_id=specialization_id, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.patch(
    "/update_by_id/{specialization_id}", status_code=status.HTTP_200_OK
)
async def update_specialization_by_id(
    specialization_id: int,
    specialization: UpdateSpecialization,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await SpecializationService.update_specialization_by_id(
            specialization_id=specialization_id,
            specialization=specialization,
            db=db,
            current_user=current_user,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.patch(
    "/soft_delete/{specialization_id}", status_code=status.HTTP_200_OK
)
async def soft_delete_specialization(
    specialization_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await SpecializationService.soft_delete_specialization(
            specialization_id=specialization_id, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.post("/create", response_model=ShowSpecialization)
async def create_specialization(
    new_specialization: CreateSpecialization,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await SpecializationService.create_specialization(
            new_specialization=new_specialization, db=db
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
