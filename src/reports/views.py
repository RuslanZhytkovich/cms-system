from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from starlette import status

from core.db import get_db
from reports.schemas import ShowReport, CreateReport, UpdateReport
from reports.services import ReportService
report_router = APIRouter()


@report_router.get("/get_all", response_model=List[ShowReport])
async def get_all_report(db: AsyncSession = Depends(get_db)):
    try:
        return await ReportService.get_all_reports_service(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.get("/get_by_id", response_model=ShowReport)
async def get_report_by_id(report_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await ReportService.get_report_by_id(report_id=report_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@report_router.delete("/delete_by_id", status_code=status.HTTP_200_OK)
async def delete_report_by_id(report_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await ReportService.delete_report_by_id(report_id=report_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.patch("/update_by_id", status_code=status.HTTP_200_OK)
async def update_report_by_id(report_id: int, report: UpdateReport, db: AsyncSession = Depends(get_db)):
    try:
        return await ReportService.update_report_by_id(report_id=report_id, report=report, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.patch("/soft_delete", status_code=status.HTTP_200_OK)
async def soft_delete_report(report_id: int, db: AsyncSession = Depends(get_db)):
    try:
        return await ReportService.soft_delete_report(report_id=report_id, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@report_router.post("/create", response_model=ShowReport)
async def create_report(new_report: CreateReport, db: AsyncSession = Depends(get_db)):
    try:
        return await ReportService.create_report(new_report=new_report, db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
