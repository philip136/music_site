from django.urls import path
from .views import (RoomApi,
                    DialogApi,
                    AddUsersRoom)


urlpatterns = [
    path('room/', RoomApi.as_view(), name='get_room'),
    path('dialog/', DialogApi.as_view(), name='get_dialog'),
    path('users_invited/', AddUsersRoom.as_view(), name='get_users'),
]