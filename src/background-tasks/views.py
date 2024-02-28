from fastapi import APIRouter

from .tasks import say_hi

router = APIRouter(prefix="/report")


@router.get("/tasks")
def get_dashboard_report():
    say_hi.delay()
