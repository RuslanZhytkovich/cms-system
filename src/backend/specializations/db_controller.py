from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


from src.backend.auth.hashing import Hasher
from src.backend.core.exceptions import DatabaseException
from src.backend.users.schemas import UserCreateRequest
from src.backend.specializations.models import Specialization


class SpecializationDBController:
    @staticmethod
    async def get_all_specializations(db: AsyncSession):
        users = await db.execute(select(Specialization))
        return users.scalars().all()
