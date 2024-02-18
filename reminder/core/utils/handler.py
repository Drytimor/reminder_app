import logging
from abc import ABCMeta

from drf_rw_serializers.generics import GenericAPIView
from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from ..serializers import EmptySerializer
from .service import EventGetService, EventPostService, RecordPostService

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler(
    filename=f"app.log", encoding='UTF-8'
)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class HandlerException(Exception):
    pass


class BaseHandler(metaclass=ABCMeta):

    exception: type[Exception] = HandlerException

    def run_service(self):
        """Запускает сервис"""
        raise NotImplementedError()


class HandlerView(GenericAPIView):

    error_text: str = 'request error'
    response_code: int
    handler: type[BaseHandler]

    serializer_class = EmptySerializer
    write_serializer_class = None
    read_serializer_class = None

    def _exception_handler(self):
        return self.handler.exception

    def run_handler(self):
        result = self.get_handler_results()
        read_serializer = self.get_read_serializer(result)

        return Response(
            read_serializer.data, status=self.response_code
        )

    def get_handler_results(self):
        kwargs = self._get_serialized_data()

        try:
            handler_object = self.handler(**kwargs)
            result = handler_object.run_service()

        except self._exception_handler() as exc:
            logger.error('validation error', exc_info=True)
            raise ValidationError(detail={'detail': exc})

        except Exception:
            logger.error('base exception', exc_info=True)
            raise APIException(detail={"detail": self.error_text})

        return result

    def _get_serialized_data(self):
        write_serializer = (
            self.get_write_serializer(
                data=self._get_data_from_request()
            )
        )
        write_serializer.is_valid(raise_exception=True)
        data = {**write_serializer.validated_data, **self.kwargs}
        return data

    def _get_data_from_request(self):
        request_data = self.request.data if self.request.data else self.request.query_params.copy()
        return request_data


class EventGetHandler(BaseHandler):

    def __init__(self, event_id: int):
        self.event_id = event_id

    def run_service(self):
        service_object = EventGetService()
        result = service_object(event_id=self.event_id)

        if result.is_error:
            raise self.exception(result.error)
        if result.is_success:
            return result.event


class EventPostHandler(BaseHandler):

    def __init__(self, name: str, date: str):
        self.name = name
        self.date = date

    def run_service(self):
        service_object = EventPostService()
        result = service_object(
            name=self.name,
            date=self.date
        )
        if result.is_error:
            raise self.exception(result.error)
        if result.is_success:
            return result.event


class RecordPostHandler(BaseHandler):
    def __init__(self, event_id: int, reminder_time: int, user_id: int):
        self.user_id = user_id
        self.event_id = event_id
        self.reminder_time = reminder_time

    def run_service(self):
        service_object = RecordPostService()
        result = service_object(
            event_id=self.event_id, reminder_time=self.reminder_time,
            user_id=self.user_id
        )
        if result.is_error:
            raise self.exception(result.error)
        if result.is_success:
            return result.record
