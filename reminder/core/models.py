from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.conf import settings

event_name_max_length = settings.EVENTS_NAME_MAX_LENGTH


class ReminderTime(models.IntegerChoices):
    zero = 0, 'не напоминать',
    one = 1, 'за один час'
    three = 3, 'за три часа'
    twelve = 12, 'за двенадцать часов'


class Events(models.Model):

    name = models.CharField(
        verbose_name='Название', max_length=event_name_max_length,
        unique=True

    )
    date = models.DateTimeField(verbose_name='Дата мероприятия')

    number_clients = models.PositiveSmallIntegerField(
        verbose_name='Количество клиентов', default=0, blank=True
    )

    def __str__(self):
        return f'{self.name}-{self.id}'

    class Meta:
        db_table = 'events'


class Records(models.Model):

    user = models.ForeignKey(
        to=AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recordings'
    )
    event = models.ForeignKey(
        to='Events', on_delete=models.CASCADE, related_name='recordings'
    )
    reminder_time = models.PositiveSmallIntegerField(
        verbose_name='Напомнить за', choices=ReminderTime.choices, default=ReminderTime.one
    )

    def __str__(self):
        return f'{self.user}-{self.event}'

    class Meta:
        db_table = 'records'

