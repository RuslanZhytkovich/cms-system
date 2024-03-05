from celery import Celery


celery = Celery("tasks", broker="redis://redis:5370")


@celery.task
def say_hi():
    print("hi" * 1000)
