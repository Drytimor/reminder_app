from celery import shared_task
from django.core.mail import send_mail


@shared_task(name='send_email')
def task_send_email(_object):
    email = _object.get('email')
    send_mail(
        "Напоминание",
        "ваше напоминание",
        "reminder.com",
        [email],
        fail_silently=False,
    )

