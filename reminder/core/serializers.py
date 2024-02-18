from rest_framework import serializers
from .models import ReminderTime, event_name_max_length


class EmptySerializer(serializers.Serializer):
    ...


class EventGetWriteSerializer(serializers.Serializer):

    event_id = serializers.IntegerField(
        label='Id евента', required=False
    )
    name = serializers.CharField(
        label='Название', max_length=event_name_max_length,
        required=False
    )
    date = serializers.DateTimeField(
        label='Дата евента', required=False
    )


class EventGetReadSerializer(serializers.Serializer):

    id = serializers.IntegerField(
        label='Id евента', read_only=True
    )
    name = serializers.CharField(
        label='Название', read_only=True
    )
    date = serializers.DateTimeField(
        label='Дата евента',  read_only=True
    )
    number_clients = serializers.IntegerField(
        label='Количество клиентов', read_only=True
    )


class EventPostWriteSerializer(serializers.Serializer):

    name = serializers.CharField(
        label='Название', max_length=10
    )
    date = serializers.DateTimeField(
        label='Дата евента'
    )


class EventPostReadSerializer(serializers.Serializer):

    id = serializers.IntegerField(
        label='Id евента'
    )
    name = serializers.CharField(
        label='Название', max_length=10
    )
    date = serializers.DateTimeField(
        label='Дата евента'
    )


class RecordGetWriteSerializer(serializers.Serializer):

    reminder_time = serializers.ChoiceField(
        label='Напомнить за', choices=ReminderTime.choices,
        default=ReminderTime.one
    )


class RecordGetReadSerializer(serializers.Serializer):

    reminder_time = serializers.IntegerField(
        label='Время напоминания'
    )


class RecordPostWriteSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(label='Id user')
    event_id = serializers.IntegerField(label='Id евента')
    reminder_time = serializers.IntegerField(label='Время напоминания')


class RecordPostReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    event = EventPostReadSerializer()
    reminder_time = serializers.IntegerField()

