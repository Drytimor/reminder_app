from rest_framework import status
from rest_framework.views import APIView

from .serializers import (
    EventGetReadSerializer, EventGetWriteSerializer, EventPostReadSerializer,
    EventPostWriteSerializer, RecordPostReadSerializer, RecordPostWriteSerializer
)
from .utils.handler import (
    HandlerView, EventGetHandler, EventPostHandler, RecordPostHandler
)


class EventView(HandlerView):

    def get(self, request, *args, **kwargs):
        self.error_text = 'Get event error'
        self.response_code = status.HTTP_200_OK
        self.read_serializer_class = EventGetReadSerializer
        self.write_serializer_class = EventGetWriteSerializer
        self.handler = EventGetHandler
        return self.run_handler()

    def post(self, request, *args, **kwargs):
        self.error_text = 'Post event error'
        self.response_code = status.HTTP_201_CREATED
        self.read_serializer_class = EventPostReadSerializer
        self.write_serializer_class = EventPostWriteSerializer
        self.handler = EventPostHandler
        return self.run_handler()

    def put(self, request, *args, **kwargs):
        ...

    def patch(self, request, *args, **kwargs):
        ...

    def delete(self, request, *args, **kwargs):
        ...


event_api = EventView.as_view()


class RecordView(HandlerView):

    def get(self, request, *args, **kwargs):
        ...

    def post(self, request, *args, **kwargs):
        self.error_text = 'record error'
        self.response_code = status.HTTP_201_CREATED
        self.read_serializer_class = RecordPostReadSerializer
        self.write_serializer_class = RecordPostWriteSerializer
        self.handler = RecordPostHandler
        return self.run_handler()

    def delete(self, request, *args, **kwargs):
        ...


record_api = RecordView.as_view()







