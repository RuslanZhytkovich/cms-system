from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_db
from reports.db_controller import ReportDBController
from reports.schemas import UpdateReport, CreateReport


class ReportService:
    @staticmethod
    async def get_all_reports_service(db: AsyncSession = Depends(get_db)):
        return await ReportDBController.get_all_reports(db=db)

    @staticmethod
    async def get_report_by_id(report_id: int, db: AsyncSession = Depends(get_db)):
        return await ReportDBController.get_report_by_id(report_id=report_id, db=db)

    @staticmethod
    async def delete_report_by_id(report_id: int, db: AsyncSession = Depends(get_db)):
        return await ReportDBController.delete_report_by_id(report_id=report_id, db=db)

    @staticmethod
    async def update_report_by_id(report_id: int, report: UpdateReport, db: AsyncSession = Depends(get_db)):
        return await ReportDBController.update_report_by_id(report_id=report_id, report=report, db=db)

    @staticmethod
    async def create_report(new_report: CreateReport, db: AsyncSession = Depends(get_db)):
        return await ReportDBController.create_report(new_report=new_report, db=db)
