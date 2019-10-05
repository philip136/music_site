from django.urls import path
from .views import (RoomApi,
                    DialogApi)


urlpatterns = [
    path('room/', RoomApi.as_view(), name='get_room'),
    path('dialog/', DialogApi.as_view(), name='get_dialog'),
]