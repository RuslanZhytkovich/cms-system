from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from starlette import status

from core.db import get_db
from projects.schemas import ShowProject, UpdateProject, CreateProject
from projects.services import ProjectService

project_router = APIRouter()


@project_router.get("/get_all", response_model=List[ShowProject])
async def get_all_projects(db: AsyncSession = Depends(get_db)):
    try:
        return await ProjectService.get_all_projects_service(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@project_router.get("/get_by_id", response_model=ShowProject)
async def get_project_by_id(project_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await ProjectService.get_project_by_id(project_id=project_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@project_router.delete("/delete_by_id", status_code=status.HTTP_200_OK)
async def delete_project_by_id(project_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await ProjectService.delete_project_by_id(project_id=project_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@project_router.patch("/update_by_id", status_code=status.HTTP_200_OK)
async def update_project_by_id(project_id: int, project: UpdateProject, db: AsyncSession = Depends(get_db)):
    try:
        return await ProjectService.update_project_by_id(project_id=project_id, project=project, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@project_router.post("/create", response_model=ShowProject)
async def create_project(new_project: CreateProject, db: AsyncSession = Depends(get_db)):
    try:
        return await ProjectService.create_project(new_project=new_project, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
