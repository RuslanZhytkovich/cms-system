from celery import Celery


celery = Celery("tasks", broker="redis://localhost:6379")


@celery.task
def say_hi():
    print("hi" * 1000)


# @celery.task
# def general_task(queue="q1"):
#     print('general task')
#     pass
#
#
# @celery.task(queue="q2")
# def generate_report_task(user_id: int, report_dicts: List[dict]):
#     directory = 'background-tasks/files'
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     user_file_path = os.path.join(directory, f'user_{user_id}.txt')
#
#     # Создание и запись данных в файл
#     with open(user_file_path, 'w') as file:
#         file.write("Date\tHours\tComment\tProject\n")
#         for report in report_dicts:
#             file.write(
#                 f"{report['date'][0]}/{report['date'][1]}/{report['date'][2]}\t{report['hours']}\t{report['comment']}\t{report['project']}\n")
#
#     print('generate_report_task is working properly')
#
#
