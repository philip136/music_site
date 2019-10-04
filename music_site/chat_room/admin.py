from django.contrib import admin
from .models import (Room,
                     Chat)



class RoomAdmin(admin.ModelAdmin):
    """Chat Room"""
    list_display = ('creater', 'invited_user', 'date')

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])


class ChatAdmin(admin.ModelAdmin):
    """ Dialog """
    list_display = ('room', 'user', 'text', 'date')

admin.site.register(Room, RoomAdmin)