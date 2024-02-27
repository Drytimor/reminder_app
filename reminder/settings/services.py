from .base import *
from kombu import Queue, Exchange

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': env('POSTGRES_HOST'),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Celery
CELERY_IMPORTS = ('core.tasks', )

CELERY_BROKER_URL = env('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_BEAT_SCHEDULER = env('CELERY_BEAT_SCHEDULER')
CELERY_WORKER_MAX_MEMORY_PER_CHILD = env.int('CELERY_WORKER_MAX_MEMORY_PER_CHILD')

create_reminder_exchange = Exchange('create_reminder', type='direct', delivery_mode='persistent')
sending_reminder_email_exchange = Exchange('sending_reminder_email', type='direct', delivery_mode='persistent')
celery = Exchange('celery', type='direct', delivery_mode='persistent')

CELERY_TASK_QUEUES = [
    Queue('create_reminder', exchange=create_reminder_exchange, routing_key='create.reminder'),
    Queue('sending_reminder_email', exchange=sending_reminder_email_exchange, routing_key='sending.reminder.email'),
    Queue('celery', exchange=celery, routing_key='celery')
]


def route_task(name, args, kwargs, options, task=None, **kw):
    match name:
        case 'create_reminder_*':
            return {
                'queue': 'create_reminder',
                'routing_key': 'create.reminder'
            }
        case 'send_reminder_by_email':
            return {
                'queue': 'sending_reminder_email',
                'routing_key': 'sending.reminder.email'
            }
        case _:
            return {
                'queue': 'celery',
                'routing_key': 'celery'
            }


CELERY_TASK_ROUTES = (route_task, )

CELERY_TASK_ANNOTATIONS = {
    'create_reminder_*': {
        'time_limit': 60*60
    },
    'send_reminder_by_email': {
        'time_limit': 60*10,
        'store_errors_even_if_ignored': True,
        'ignore_result': True
    },
    'add': {
        'store_errors_even_if_ignored': True,
        'ignore_result': True,
        'time_limit': 60
    }
}



