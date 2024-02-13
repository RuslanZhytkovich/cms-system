from core.db import get_db
from core.exceptions import InvalidPermissionsException
from fastapi import Depends
from reports.db_controller import ReportDBController
from reports.schemas import CreateReport
from reports.schemas import UpdateReport
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import Permission


class ReportService:
    @staticmethod
    async def get_all_reports_service(
        current_user: User, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await ReportDBController.get_all_reports(db=db)

    @staticmethod
    async def get_report_by_id(
        current_user: User, report_id: int, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await ReportDBController.get_report_by_id(report_id=report_id, db=db)

    @staticmethod
    async def delete_report_by_id(
        current_user: User, report_id: int, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await ReportDBController.delete_report_by_id(report_id=report_id, db=db)

    @staticmethod
    async def update_report_by_id(
        current_user: User,
        report_id: int,
        report: UpdateReport,
        db: AsyncSession = Depends(get_db),
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await ReportDBController.update_report_by_id(
            report_id=report_id, report=report, db=db
        )

    @staticmethod
    async def soft_delete_report(
        current_user: User, report_id: int, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await ReportDBController.soft_delete(report_id=report_id, db=db)

    @staticmethod
    async def create_report(
        current_user: User, new_report: CreateReport, db: AsyncSession = Depends(get_db)
    ):
        if not Permission.check_admin_manager_permissions(current_user=current_user):
            raise InvalidPermissionsException()
        return await ReportDBController.create_report(new_report=new_report, db=db)
