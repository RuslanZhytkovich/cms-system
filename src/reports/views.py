from typing import List

from auth.services import AuthService
from core.db import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from reports.schemas import CreateReport
from reports.schemas import ShowReport
from reports.schemas import UpdateReport
from reports.services import ReportService
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from users.models import User

report_router = APIRouter()


@report_router.get("/get_all", response_model=List[ShowReport])
async def get_all_report(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await ReportService.get_all_reports_service(
            db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.get("/get_by_id/{report_id}", response_model=ShowReport)
async def get_report_by_id(
    report_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await ReportService.get_report_by_id(
            report_id=report_id, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@report_router.delete("/delete_by_id/{report_id}", status_code=status.HTTP_200_OK)
async def delete_report_by_id(
    report_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await ReportService.delete_report_by_id(
            report_id=report_id, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.patch("/update_by_id/{report_id}", status_code=status.HTTP_200_OK)
async def update_report_by_id(
    report_id: int,
    report: UpdateReport,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await ReportService.update_report_by_id(
            report_id=report_id, report=report, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.patch("/soft_delete/{report_id}", status_code=status.HTTP_200_OK)
async def soft_delete_report(
    report_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await ReportService.soft_delete_report(
            report_id=report_id, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.post("/create", response_model=ShowReport)
async def create_report(
    new_report: CreateReport,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(AuthService.get_current_user_from_token),
):
    try:
        return await ReportService.create_report(
            new_report=new_report, db=db, current_user=current_user
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
