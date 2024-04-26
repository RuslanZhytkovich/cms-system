from core.db import get_db
from core.exceptions import NotFoundException, AlreadyExist
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
    async def get_all_specializations_service(
        current_user: User, db: AsyncSession
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
    async def get_specialization_by_id(
        current_user: User, specialization_id: int, db: AsyncSession
    ):
        if cache := await RedisRepository.get_from_redis(
            f"specialization{specialization_id}"
        ):
            return Specialization(**jsonable_encoder(cache))
        else:
            specialization = await SpecializationDBController.get_specialization_by_id(
                specialization_id=specialization_id, db=db
            )
            if not specialization:
                raise NotFoundException
            await RedisRepository.set_to_redis(
                key=f"specialization{specialization_id}",
                value=jsonable_encoder(specialization),
                expire_seconds=86400,
            )
            return specialization

    @staticmethod
    async def get_specialization_by_name(
            current_user: User, specialization_name: str, db: AsyncSession
    ):
        specialization = await SpecializationDBController.get_specialization_by_name(specialization_name=specialization_name, db=db)
        if not specialization:
            raise NotFoundException
        return specialization

    @staticmethod
    @check_admin_manager_permission
    async def delete_specialization_by_id(
        current_user: User, specialization_id: int, db: AsyncSession
    ):
        specialization = await SpecializationDBController.get_specialization_by_id(specialization_id=specialization_id, db=db)
        if not specialization:
            raise NotFoundException
        await RedisRepository.clear_key("specializations")
        await RedisRepository.clear_key("users")
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
        db: AsyncSession
    ):
        specialization_from_db = await SpecializationDBController.get_specialization_by_id(specialization_id=specialization_id,
                                                                                   db=db)
        if not specialization_from_db:
            raise NotFoundException
        await RedisRepository.clear_key("specializations")
        await RedisRepository.clear_key("users")
        await RedisRepository.clear_key(f"specialization{specialization_id}")
        return await SpecializationDBController.update_specialization_by_id(
            specialization_id=specialization_id, specialization=specialization, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def soft_delete_specialization(
        current_user: User, specialization_id: int, db: AsyncSession
    ):
        specialization = await SpecializationDBController.get_specialization_by_id(specialization_id=specialization_id,
                                                                                   db=db)
        if not specialization:
            raise NotFoundException
        await RedisRepository.clear_key("specializations")
        await RedisRepository.clear_key("users")
        await RedisRepository.clear_key(f"specialization{specialization_id}")
        return await SpecializationDBController.soft_delete(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def create_specialization(
        current_user: User,
        new_specialization: CreateSpecialization,
        db: AsyncSession
    ):
        specialization = await SpecializationDBController.get_specialization_by_name(specialization_name=new_specialization.specialization_name, db=db)
        if specialization:
            raise AlreadyExist
        await RedisRepository.clear_key("specializations")
        return await SpecializationDBController.create_specialization(
            new_specialization=new_specialization, db=db
        )
