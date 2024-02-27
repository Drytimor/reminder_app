from django.urls import path
from .api import event_api, record_api

urlpatterns = [
    path('event/', event_api),
    path('record/', record_api),
]