from celery import shared_task
from django.core.mail import send_mail
from .models import ReminderTime, Records
from django_celery_beat.models import PeriodicTask, ClockedSchedule
import datetime
import logging
import json


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(
    filename=f"app.log", encoding='UTF-8'
)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


@shared_task(bind=True, name='create_reminder_for_user_one_hours')
def task_create_reminder_for_user_one_hour(self, date: 'datetime', event_id: int):

    reminder_time = ReminderTime.one
    clocked_time = datetime.datetime.now() + datetime.timedelta(minutes=float(reminder_time))
    one_hour_clocked_schedule = ClockedSchedule.objects.create(
        clocked_time=clocked_time
    )
    one_hour_reminder_task = PeriodicTask.objects.create(
        name='one_hour_reminder_event_{}_task'.format(event_id),
        task='send_reminder_by_email',
        args=json.dumps([reminder_time, event_id]),
        clocked=one_hour_clocked_schedule,
        one_off=True
    )
    logger.info('timelimit: {0.timelimit!r}, headers: {0.headers!r}'.format(self.request))


@shared_task(bind=True, name='create_reminder_for_user_three_hours')
def task_create_reminder_for_user_three_hours(self, date: 'datetime', event_id: int):

    reminder_time = ReminderTime.three
    clocked_time = datetime.datetime.now() + datetime.timedelta(minutes=float(reminder_time))

    free_hour_clocked_schedule = ClockedSchedule.objects.create(
        clocked_time=clocked_time
    )
    free_hour_reminder_task = PeriodicTask.objects.create(
        name='three_hour_reminder_event_{}_task'.format(event_id),
        task='send_reminder_by_email',
        args=json.dumps([reminder_time, event_id]),
        clocked=free_hour_clocked_schedule,
        one_off=True
    )


@shared_task(bind=True, name='create_reminder_for_user_twelve_hours')
def task_create_reminder_for_user_twelve_hours(self, date: 'datetime', event_id: int):

    reminder_time = ReminderTime.twelve
    clocked_time = datetime.datetime.now() + datetime.timedelta(minutes=float(reminder_time))

    twelve_hour_clocked_schedule = ClockedSchedule.objects.create(
        clocked_time=clocked_time
    )
    twelve_hour_reminder_task = PeriodicTask.objects.create(
        name='twelve_hour_reminder_event_{}_task'.format(event_id),
        task='send_reminder_by_email',
        args=json.dumps([reminder_time, event_id]),
        clocked=twelve_hour_clocked_schedule,
        one_off=True
    )


@shared_task(bind=True, name='send_reminder_by_email')
def task_send_reminder_by_email(self, reminder_time: int, event_id: int):
    user_email = (
        Records.objects.filter(
            event=event_id, reminder_time=reminder_time
        ).values_list('user__email', flat=True)
    )
    logger.info('user_email: {}'.format(user_email))
    send_mail(
        "Напоминание",
        "ваше напоминание event_id: {}".format(event_id),
        "reminder.com",
        user_email,
        fail_silently=False,
    )

