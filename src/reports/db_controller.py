from core.exceptions import DatabaseException
from customers.models import Customer
from projects.models import Project
from reports.models import Report
from reports.schemas import CreateReport
from reports.schemas import UpdateReport
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession


class ReportDBController:
    @staticmethod
    async def get_all_reports(db: AsyncSession):
        try:
            reports = await db.execute(
                select(Report)
                .join(Project)
                .filter(Project.is_deleted == False)
                .filter(Report.is_deleted == False)
            )
            return reports.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_report_by_id(db: AsyncSession, report_id: int):
        try:
            query = (
                select(Report)
                .join(Project)
                .where(
                    (Report.report_id == report_id) & (Project.is_deleted == False) & (Report.is_deleted == False))
            )
            project = await db.execute(query)
            return project.scalar()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_reports_by_user_id(db: AsyncSession, user_id: int):
        try:
            query = (
                select(Report)
                .join(Project)
                .join(Customer)
                .where(
                    (Report.user_id == user_id) & (Report.is_deleted == False) &
                    (Project.is_deleted == False) & (Customer.is_deleted == False)
                )
            )
            report = await db.execute(query)
            return report.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def delete_report_by_id(db: AsyncSession, report_id: int):
        try:
            query = delete(Report).where(Report.report_id == report_id)
            await db.execute(query)
            await db.commit()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def create_report(db: AsyncSession, new_report: CreateReport, user_id):
        try:
            query = (
                insert(Report)
                .values(**new_report.dict(), user_id=user_id)
                .returning(Report)
            )
            result = await db.execute(query)
            new_report = result.scalar()
            await db.commit()
            return new_report
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_report_by_id(
        report_id: int, report: UpdateReport, db: AsyncSession
    ):
        try:
            query = (
                update(Report)
                .where(Report.report_id == report_id)
                .values(**report.dict(exclude_none=True))
                .returning(Report)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def soft_delete(report_id: int, db: AsyncSession):
        try:
            query = (
                update(Report)
                .where(Report.report_id == report_id)
                .values(is_deleted=True)
                .returning(Report)
            )
            result = await db.execute(query)
            updated = result.scalar()
            await db.commit()
            return updated

        except Exception:
            raise DatabaseException
