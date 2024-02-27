from django.contrib import admin
from .models import Events, Records


@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass

