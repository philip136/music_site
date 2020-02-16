from django.contrib import admin
from .models import (Album,
                     SongsAlbum,
                     Person,
                     Vote,
                     Comments)
from django.utils.safestring import mark_safe



@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("author_album",
                    "name_album",
                    "author",
                    "get_image",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image_album.url} width='100' height='auto'")



admin.site.register(SongsAlbum)
admin.site.register(Person)
admin.site.register(Vote)
admin.site.register(Comments)

