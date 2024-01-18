from sqlalchemy import Float, UUID
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.sql import func
from src.backend.core.db import Base


class Report(Base):
    __tablename__ = "reports"

    report_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    date = Column(Date, server_default=func.now(), nullable=True)
    hours = Column(Float, nullable=False)
    comment = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.user_id'))
    project_id = Column(Integer, ForeignKey('projects.project_id'))