from core.db import get_db
from fastapi import Depends
from projects.db_controller import ProjectDBController
from projects.schemas import CreateProject
from projects.schemas import UpdateProject
from sqlalchemy.ext.asyncio import AsyncSession


class ProjectService:
    @staticmethod
    async def get_all_projects_service(db: AsyncSession = Depends(get_db)):
        return await ProjectDBController.get_all_projects(db=db)

    @staticmethod
    async def get_project_by_id(project_id: int, db: AsyncSession = Depends(get_db)):
        return await ProjectDBController.get_project_by_id(project_id=project_id, db=db)

    @staticmethod
    async def delete_project_by_id(project_id: int, db: AsyncSession = Depends(get_db)):
        return await ProjectDBController.delete_project_by_id(
            project_id=project_id, db=db
        )

    @staticmethod
    async def update_project_by_id(
        project_id: int, project: UpdateProject, db: AsyncSession = Depends(get_db)
    ):
        return await ProjectDBController.update_project_by_id(
            project_id=project_id, project=project, db=db
        )

    @staticmethod
    async def soft_delete_project(project_id: int, db: AsyncSession = Depends(get_db)):
        return await ProjectDBController.soft_delete(project_id=project_id, db=db)

    @staticmethod
    async def create_project(
        new_project: CreateProject, db: AsyncSession = Depends(get_db)
    ):
        return await ProjectDBController.create_project(new_project=new_project, db=db)
