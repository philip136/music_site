from django.contrib import admin
from .models import Album,SongsAlbum,Person,Vote


admin.site.register(Album)
admin.site.register(SongsAlbum)
admin.site.register(Person)
admin.site.register(Vote)