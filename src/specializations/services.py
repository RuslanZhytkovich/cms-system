from core.db import get_db
from core.exceptions import InvalidPermissionsException
from fastapi import Depends
from specializations.db_controller import SpecializationDBController
from specializations.schemas import CreateSpecialization
from specializations.schemas import UpdateSpecialization
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import Permission


class SpecializationService:
    @staticmethod
    async def get_all_specializations_service(
        current_user: User, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await SpecializationDBController.get_all_specializations(db=db)

    @staticmethod
    async def get_specialization_by_id(
        current_user: User, specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await SpecializationDBController.get_specialization_by_id(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    async def delete_specialization_by_id(
        current_user: User, specialization_id: int, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await SpecializationDBController.delete_specialization_by_id(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    async def update_specialization_by_id(
        current_user: User,
        specialization_id: int,
        specialization: UpdateSpecialization,
        db: AsyncSession = Depends(get_db),
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await SpecializationDBController.update_specialization_by_id(
            specialization_id=specialization_id, specialization=specialization, db=db
        )

    @staticmethod
    async def soft_delete_specialization(
        current_user: User,
        specialization_id: int,
        db: AsyncSession = Depends(get_db),
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await SpecializationDBController.soft_delete(
            specialization_id=specialization_id, db=db
        )

    @staticmethod
    async def create_specialization(
        new_specialization: CreateSpecialization,
        db: AsyncSession = Depends(get_db),
    ):

        return await SpecializationDBController.create_specialization(
            new_specialization=new_specialization, db=db
        )
