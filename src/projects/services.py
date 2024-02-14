from core.db import get_db
from core.exceptions import InvalidPermissionsException
from fastapi import Depends
from projects.db_controller import ProjectDBController
from projects.schemas import CreateProject
from projects.schemas import UpdateProject
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import Permission, check_admin_manager_permission


class ProjectService:
    @staticmethod
    @check_admin_manager_permission
    async def get_all_projects_service(
        current_user: User, db: AsyncSession = Depends(get_db)
    ):
        return await ProjectDBController.get_all_projects(db=db)

    @staticmethod
    @check_admin_manager_permission
    async def get_project_by_id(
        current_user: User, project_id: int, db: AsyncSession = Depends(get_db)
    ):

        return await ProjectDBController.get_project_by_id(project_id=project_id, db=db)

    @staticmethod
    @check_admin_manager_permission
    async def delete_project_by_id(
        current_user: User, project_id: int, db: AsyncSession = Depends(get_db)
    ):
        return await ProjectDBController.delete_project_by_id(
            project_id=project_id, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def update_project_by_id(
        current_user: User,
        project_id: int,
        project: UpdateProject,
        db: AsyncSession = Depends(get_db),
    ):

        return await ProjectDBController.update_project_by_id(
            project_id=project_id, project=project, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def soft_delete_project(
        current_user: User, project_id: int, db: AsyncSession = Depends(get_db)
    ):

        return await ProjectDBController.soft_delete(project_id=project_id, db=db)

    @staticmethod
    @check_admin_manager_permission
    async def create_project(
        current_user: User,
        new_project: CreateProject,
        db: AsyncSession = Depends(get_db),
    ):
        return await ProjectDBController.create_project(new_project=new_project, db=db)
