from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db import get_db
from src.specializations.schemas import CreateSpecialization, UpdateSpecialization, ShowSpecialization
from src.specializations.services import SpecializationService

specialization_router = APIRouter()


@specialization_router.get("/get_all", response_model=List[ShowSpecialization])
async def get_all_specializations(db: AsyncSession = Depends(get_db)):
    try:
        return await SpecializationService.get_all_specializations_service(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.get("/get_by_id", response_model=ShowSpecialization)
async def get_specialization_by_id(specialization_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await SpecializationService.get_specialization_by_id(specialization_id=specialization_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.delete("/delete_by_id", status_code=status.HTTP_200_OK)
async def delete_specialization_by_id(specialization_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await SpecializationService.delete_specialization_by_id(specialization_id=specialization_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.patch("/update_by_id", status_code=status.HTTP_200_OK)
async def update_specialization_by_id(specialization_id: int, specialization: UpdateSpecialization,
                                      db: AsyncSession = Depends(get_db)):
    try:
        return await SpecializationService.update_specialization_by_id(specialization_id=specialization_id,
                                                                       specialization=specialization, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@specialization_router.post("/create", response_model=ShowSpecialization)
async def create_specialization(new_specialization: CreateSpecialization, db: AsyncSession = Depends(get_db)):
    try:
        return await SpecializationService.create_specialization(new_specialization=new_specialization, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
