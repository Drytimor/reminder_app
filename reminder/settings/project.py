from .base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EVENTS_NAME_MAX_LENGTH = env.int('EVENTS_NAME_MAX_LENGTH')
