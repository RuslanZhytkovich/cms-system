from core.exceptions import DatabaseException
from specializations.models import Specialization
from specializations.schemas import CreateSpecialization
from specializations.schemas import UpdateSpecialization
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession


class SpecializationDBController:
    @staticmethod
    async def get_all_specializations(db: AsyncSession):
        try:
            specialization = await db.execute(select(Specialization))
            return specialization.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_specialization_by_id(db: AsyncSession, specialization_id: int):
        try:
            query = select(Specialization).where(
                Specialization.specialization_id == specialization_id
            )
            specialization = await db.execute(query)
            return specialization.scalar()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def delete_specialization_by_id(db: AsyncSession, specialization_id: int):
        try:
            query = delete(Specialization).where(
                Specialization.specialization_id == specialization_id
            )
            await db.execute(query)
            await db.commit()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def create_specialization(
        db: AsyncSession, new_specialization: CreateSpecialization
    ):
        try:
            query = (
                insert(Specialization)
                .values(**new_specialization.dict())
                .returning(Specialization)
            )
            result = await db.execute(query)
            new_specialization = result.scalar()
            await db.commit()
            return new_specialization
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_specialization_by_id(
        specialization_id: int, specialization: UpdateSpecialization, db: AsyncSession
    ):
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

    @staticmethod
    async def soft_delete(specialization_id: int, db: AsyncSession):
        try:
            query = (
                update(Specialization)
                .where(Specialization.specialization_id == specialization_id)
                .values(is_deleted=True)
                .returning(Specialization)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated

        except Exception:
            raise DatabaseException
