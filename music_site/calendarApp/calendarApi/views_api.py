from rest_framework.generics import (CreateAPIView,
                                    RetrieveAPIView,
                                     ListAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     )
from rest_framework.response import Response
from .serializer_api import (CalendarSerializer,
                             CalendarListSerializer,
                             CalendarUpdateSerializer,
                             CalendarDeleteSerializer)
from calendarApp.models import Calendar
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect


class CalendarListApi(ListAPIView):
    queryset = Calendar.objects.all().order_by('-start_event')
    serializer_class = CalendarListSerializer
    permission_classes = [IsAuthenticated]


class CalendarViewApi(CreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, template_name="calendarApp/calendar.html")


class CalendarUpdateEventApi(UpdateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, event_id):
        try:
            calendar = Calendar.objects.get(id=event_id)
            return calendar
        except Calendar.DoesNotExist:
            raise Http404

    def get(self, request, event_id, *args, **kwargs):
        calendar = self.get_object(event_id)
        serializer = self.serializer_class(calendar)
        return Response(serializer.data)


    def update(self, request, event_id, *args, **kwargs):
        calendar = Calendar.objects.get(id=event_id)
        serializer = self.serializer_class(calendar, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CalendarDeleteEventApi(DestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarDeleteSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, event_id):
        try:
            calendar = Calendar.objects.get(id=event_id)
            return calendar
        except Calendar.DoesNotExist:
            raise Http404

    def get(self, request, event_id, *args, **kwargs):
        calendar = self.get_object(event_id)
        serializer = self.serializer_class(calendar)
        return Response(serializer.data)

    def destroy(self, request, event_id,  *args, **kwargs):
        try:
            calendar = self.get_object(event_id)
            self.perform_destroy(calendar)
        except Calendar.DoesNotExist:
            raise Http404
        return Response(status=status.HTTP_200_OK)