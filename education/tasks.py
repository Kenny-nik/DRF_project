from celery import shared_task
# from education.models import Subscription
from django.core.mail import send_mail
# from config import settings
from users.models import User
from django.utils import timezone
from datetime import timedelta


@shared_task
def last_visit():
    users = User.objects.filter(last_login__isnll=False)
    for user in users:
        if timezone.now() - user.last_login > timedelta(days=30):
            user.is_active = False
            print(f"Блокировка {user.email}")
            user.save()


@shared_task
def update_course_mail(course_id):
    from education.models import Course

    course = Course.objects.get(pk=course_id)
    send_mail(
        subject=f"Курс {course.title} обновлён",
        message=f"Описание: {course.description}",
        from_email="admin@example.com",
        recipient_list=["user@example.com"],
    )


# def update_course_mail(course_id):
#     subscription_course = Subscription.objects.filter(course=course_id)
#     sub_list = [sub.user.email for sub in subscription_course]
#     if sub_list:
#         subject = f"Изменение курса {subscription_course.first().course.title}"
#         message = f"Курс {subscription_course.first().course.title} изменен."
#         send_mail(
#             subject,
#             message,
#             settings.DEFAULT_FROM_EMAIL,
#             sub_list,
#             fail_silently=False,
#         )
