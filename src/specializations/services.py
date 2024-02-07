from core.db import get_db
from fastapi import Depends
from specializations.db_controller import SpecializationDBController
from specializations.schemas import CreateSpecialization
from specializations.schemas import UpdateSpecialization
from sqlalchemy.ext.asyncio import AsyncSession


class SpecializationService:
    @staticmethod
    async def get_all_specializations_service(db: AsyncSession = Depends(get_db)):
        return await SpecializationDBController.get_all_specializations(db=db)

    @staticmethod
    async def get_specialization_by_id(
        specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        return await SpecializationDBController.get_specialization_by_id(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    async def delete_specialization_by_id(
        specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        return await SpecializationDBController.delete_specialization_by_id(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    async def update_specialization_by_id(
        specialization_id: int,
        specialization: UpdateSpecialization,
        db: AsyncSession = Depends(get_db),
    ):
        return await SpecializationDBController.update_specialization_by_id(
            specialization_id=specialization_id, specialization=specialization, db=db
        )

    @staticmethod
    async def soft_delete_specialization(
        specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        return await SpecializationDBController.soft_delete(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    async def create_specialization(
        new_specialization: CreateSpecialization, db: AsyncSession = Depends(get_db)
    ):
        return await SpecializationDBController.create_specialization(
            new_specialization=new_specialization, db=db
        )
