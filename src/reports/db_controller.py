from sqlalchemy import select, delete, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.exceptions import DatabaseException
from reports.models import Report
from reports.schemas import CreateReport, UpdateReport


class ReportDBController:
    @staticmethod
    async def get_all_reports(db: AsyncSession):
        try:
            reports = await db.execute(select(Report))
            return reports.scalars().all()
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def get_report_by_id(db: AsyncSession, report_id: int):
        try:
            query = select(Report).where(Report.report_id == report_id)
            report = await db.execute(query)
            return report.scalar()
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
    async def create_report(db: AsyncSession, new_report: CreateReport):
        try:
            query = insert(Report).values(**new_report.dict()).returning(Report)
            result = await db.execute(query)
            new_report = result.scalar()
            await db.commit()
            return new_report
        except Exception as e:
            raise DatabaseException(str(e))

    @staticmethod
    async def update_report_by_id(report_id: int, report: UpdateReport, db: AsyncSession):
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







