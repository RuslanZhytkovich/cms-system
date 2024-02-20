from core.db import get_db
from core.redis_repository import RedisRepository
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from specializations.db_controller import SpecializationDBController
from specializations.models import Specialization
from specializations.schemas import CreateSpecialization
from specializations.schemas import UpdateSpecialization
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import check_admin_manager_permission


class SpecializationService:
    @staticmethod
    @check_admin_manager_permission
    async def get_all_specializations_service(
        current_user: User, db: AsyncSession = Depends(get_db)
    ):
        if cache := await RedisRepository.get_from_redis("specializations"):

            return [
                Specialization(**specialization)
                for specialization in jsonable_encoder(cache)
            ]
        else:

            specializations = await SpecializationDBController.get_all_specializations(
                db
            )
            specializations_data = [
                jsonable_encoder(specialization) for specialization in specializations
            ]
            await RedisRepository.set_to_redis(
                "specializations", specializations_data, expire_seconds=86400
            )
            return specializations_data

    @staticmethod
    @check_admin_manager_permission
    async def get_specialization_by_id(
        current_user: User, specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        if cache := await RedisRepository.get_from_redis(
            f"specialization{specialization_id}"
        ):
            return Specialization(**jsonable_encoder(cache))
        else:
            specialization = await SpecializationDBController.get_specialization_by_id(
                specialization_id=specialization_id, db=db
            )
            await RedisRepository.set_to_redis(
                key=f"specialization{specialization_id}",
                value=jsonable_encoder(specialization),
                expire_seconds=86400,
            )
            return specialization

    @staticmethod
    @check_admin_manager_permission
    async def delete_specialization_by_id(
        current_user: User, specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        await RedisRepository.clear_key("specializations")
        await RedisRepository.clear_key(f"specialization{specialization_id}")
        return await SpecializationDBController.delete_specialization_by_id(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def update_specialization_by_id(
        current_user: User,
        specialization_id: int,
        specialization: UpdateSpecialization,
        db: AsyncSession = Depends(get_db),
    ):
        await RedisRepository.clear_key("specializations")
        await RedisRepository.clear_key(f"specialization{specialization_id}")
        return await SpecializationDBController.update_specialization_by_id(
            specialization_id=specialization_id, specialization=specialization, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def soft_delete_specialization(
        current_user: User, specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        await RedisRepository.clear_key("specializations")
        await RedisRepository.clear_key(f"specialization{specialization_id}")
        return await SpecializationDBController.soft_delete(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def create_specialization(
        current_user: User,
        new_specialization: CreateSpecialization,
        db: AsyncSession = Depends(get_db),
    ):
        await RedisRepository.clear_key("specializations")
        return await SpecializationDBController.create_specialization(
            new_specialization=new_specialization, db=db
        )
