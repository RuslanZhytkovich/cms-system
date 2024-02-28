from core.exceptions import NotFoundException
from reports.db_controller import ReportDBController
from reports.schemas import CreateReport
from reports.schemas import UpdateReport
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import User
from utils.permissions import check_admin_manager_permission


class ReportService:
    @check_admin_manager_permission
    @staticmethod
    async def get_all_reports_service(current_user: User, db: AsyncSession):
        return await ReportDBController.get_all_reports(db=db)

    @staticmethod
    @check_admin_manager_permission
    async def get_report_by_id(current_user: User, report_id: int, db: AsyncSession):
        report = await ReportDBController.get_report_by_id(report_id=report_id, db=db)
        if not report:
            raise NotFoundException
        return report

    @staticmethod
    async def get_my_reports(current_user: User, db: AsyncSession):
        reports = await ReportDBController.get_reports_by_user_id(
            user_id=current_user.user_id, db=db
        )
        if not reports:
            raise NotFoundException
        return reports

    @staticmethod
    @check_admin_manager_permission
    async def delete_report_by_id(current_user: User, report_id: int, db: AsyncSession):
        report_from_db = await ReportDBController.get_report_by_id(
            report_id=report_id, db=db
        )
        if not report_from_db:
            raise NotFoundException

        return await ReportDBController.delete_report_by_id(report_id=report_id, db=db)

    @staticmethod
    @check_admin_manager_permission
    async def update_report_by_id(
        current_user: User, report_id: int, report: UpdateReport, db: AsyncSession
    ):
        report_from_db = await ReportDBController.get_report_by_id(
            report_id=report_id, db=db
        )
        if not report_from_db:
            raise NotFoundException
        return await ReportDBController.update_report_by_id(
            report_id=report_id, report=report, db=db
        )

    @staticmethod
    @check_admin_manager_permission
    async def soft_delete_report(current_user: User, report_id: int, db: AsyncSession):
        report_from_db = await ReportDBController.get_report_by_id(
            report_id=report_id, db=db
        )
        if not report_from_db:
            raise NotFoundException
        return await ReportDBController.soft_delete(report_id=report_id, db=db)

    @staticmethod
    async def create_report(
        current_user: User, new_report: CreateReport, db: AsyncSession
    ):

        return await ReportDBController.create_report(
            new_report=new_report, db=db, user_id=current_user.user_id
        )
