from typing import List

from auth.services import AuthService
from core.db import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from projects.schemas import CreateProject
from projects.schemas import ShowProject
from projects.schemas import UpdateProject
from projects.services import ProjectService
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from users.models import User

project_router = APIRouter()


@project_router.get("/get_all", response_model=List[ShowProject])
async def get_all_projects(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):

    return await ProjectService.get_all_projects_service(
        db, current_user=current_user
    )



@project_router.get("/get_by_id/{project_id}", response_model=ShowProject)
async def get_project_by_id(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):

    return await ProjectService.get_project_by_id(
        project_id=project_id, db=db, current_user=current_user
    )


@project_router.delete("/delete_by_id/{project_id}", status_code=status.HTTP_200_OK)
async def delete_project_by_id(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):

    return await ProjectService.delete_project_by_id(
        project_id=project_id, db=db, current_user=current_user
    )



@project_router.patch("/update_by_id/{project_id}", status_code=status.HTTP_200_OK)
async def update_project_by_id(
    project_id: int,
    project: UpdateProject,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):

    return await ProjectService.update_project_by_id(
        project_id=project_id, project=project, db=db, current_user=current_user
    )


@project_router.patch("/soft_delete/{project_id}", status_code=status.HTTP_200_OK)
async def soft_delete_project(
    project_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):

    return await ProjectService.soft_delete_project(
        project_id=project_id, db=db, current_user=current_user
    )



@project_router.post("/create", response_model=ShowProject)
async def create_project(
    new_project: CreateProject,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):

    return await ProjectService.create_project(
        new_project=new_project, db=db, current_user=current_user
    )
