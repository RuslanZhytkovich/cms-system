from core.db import get_db
from core.exceptions import NotFoundException, AlreadyExist
from core.redis_repository import RedisRepository
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from projects.db_controller import ProjectDBController
from projects.models import Project
from projects.schemas import CreateProject
from projects.schemas import UpdateProject
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import check_admin_manager_permission


class ProjectService:
    @staticmethod
    @check_admin_manager_permission
    async def get_all_projects_service(
        current_user: User, db: AsyncSession = Depends(get_db)
    ):
        if cache := await RedisRepository.get_from_redis("projects"):

            return [Project(**project) for project in jsonable_encoder(cache)]
        else:

            projects = await ProjectDBController.get_all_projects(db)
            projects_data = [jsonable_encoder(project) for project in projects]
            await RedisRepository.set_to_redis(
                "projects", projects_data, expire_seconds=86400
            )
            return projects_data

    @staticmethod
    @check_admin_manager_permission
    async def get_project_by_id(
        current_user: User, project_id: int, db: AsyncSession = Depends(get_db)
    ):
        if cache := await RedisRepository.get_from_redis(f"project{project_id}"):
            return Project(**jsonable_encoder(cache))
        else:
            project = await ProjectDBController.get_project_by_id(project_id=project_id, db=db)
            if not project:
                raise NotFoundException
            await RedisRepository.set_to_redis(
                key=f"project{project_id}",
                value=jsonable_encoder(project),
                expire_seconds=86400,
            )
            return project

    @staticmethod
    @check_admin_manager_permission
    async def get_project_by_name(
            current_user: User, project_name: str, db: AsyncSession = Depends(get_db)
    ):
        project = await ProjectDBController.get_project_by_name(project_name=project_name, db=db)
        if not project:
            raise NotFoundException
        return project

    @staticmethod
    @check_admin_manager_permission
    async def delete_project_by_id(
        current_user: User, project_id: int, db: AsyncSession = Depends(get_db)
    ):
        project = await ProjectDBController.get_project_by_id(project_id=project_id, db=db)
        if not project:
            raise NotFoundException

        await RedisRepository.clear_key("projects")
        await RedisRepository.clear_key(f"project{project_id}")
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
        project = await ProjectDBController.get_project_by_id(project_id=project_id, db=db)
        if not project:
            raise NotFoundException
        await RedisRepository.clear_key("projects")
        await RedisRepository.clear_key(f"project{project_id}")
        return await ProjectDBController.update_project_by_id(
            project_id=project_id, project=project, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def soft_delete_project(
        current_user: User, project_id: int, db: AsyncSession = Depends(get_db)
    ):
        project = await ProjectDBController.get_project_by_id(project_id=project_id, db=db)
        if not project:
            raise NotFoundException
        await RedisRepository.clear_key("projects")
        await RedisRepository.clear_key(f"project{project_id}")
        return await ProjectDBController.soft_delete(project_id=project_id, db=db)

    @staticmethod
    @check_admin_manager_permission
    async def create_project(
        current_user: User,
        new_project: CreateProject,
        db: AsyncSession = Depends(get_db),
    ):
        project = await ProjectDBController.get_project_by_name(project_name=new_project.project_name, db=db)
        if project:
            raise AlreadyExist
        await RedisRepository.clear_key("projects")
        return await ProjectDBController.create_project(new_project=new_project, db=db)
