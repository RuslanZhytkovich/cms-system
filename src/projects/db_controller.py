from sqlalchemy import select, delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import DatabaseException
from src.projects.models import Project
from src.projects.schemas import CreateProject, UpdateProject


class ProjectDBController:
    @staticmethod
    async def get_all_projects(db: AsyncSession):
        try:
            projects = await db.execute(select(Project))
            return projects.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_project_by_id(db: AsyncSession, project_id: int):
        try:
            query = select(Project).where(Project.project_id == project_id)
            customer = await db.execute(query)
            return customer.scalar()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def delete_project_by_id(db: AsyncSession, project_id: int):
        try:
            query = delete(Project).where(Project.project_id == project_id)
            await db.execute(query)
            await db.commit()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def create_project(db: AsyncSession, new_project: CreateProject):
        try:
            query = insert(Project).values(**new_project.dict()).returning(Project)
            result = await db.execute(query)
            new_project = result.scalar()
            await db.commit()
            return new_project
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_project_by_id(project_id: int, project: UpdateProject, db: AsyncSession):
        try:
            query = (
                update(Project)
                .where(Project.project_id == project_id)
                .values(**project.dict(exclude_none=True))
                .returning(Project)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated
        except Exception as e:
            raise DatabaseException(str(e))






