from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.backend.core.exceptions import DatabaseException
from src.backend.specializations.models import Specialization
from src.backend.specializations.schemas import CreateSpecialization, UpdateSpecialization


class SpecializationDBController:
    @staticmethod
    async def get_all_specializations(db: AsyncSession):
        try:
            query = select(Specialization)
            specialization = await db.execute(query)
            return specialization.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_specialization_by_id(db: AsyncSession, specialization_id: int):
        try:
            query = select(Specialization).where(Specialization.specialization_id == specialization_id)
            specialization = await db.execute(query)
            return specialization.scalar()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def delete_specialization_by_id(db: AsyncSession, specialization_id: int):
        try:
            query = delete(Specialization).where(Specialization.specialization_id == specialization_id)
            await db.execute(query)
            await db.commit()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def create_specialization(db: AsyncSession, new_specialization: CreateSpecialization):
        try:
            query = insert(Specialization).values(**new_specialization.dict()).returning(Specialization)
            result = await db.execute(query)
            new_specialization = result.scalar()
            await db.commit()
            return new_specialization
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_specialization_by_id(specialization_id: int, specialization: UpdateSpecialization,
                                          db: AsyncSession):
        try:
            query = (
                update(Specialization)
                .where(Specialization.specialization_id == specialization_id)
                .values(**specialization.dict(exclude_none=True))
                .returning(Specialization)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated
        except Exception as e:
            raise DatabaseException(str(e))
