from django.urls import path
from .views import (AlbumList,
                    HomePage,
                    SongAlbum,
                    UpdateVote,
                    CreateVote,
                    TopAlbum,
                    Categories)

app_name = 'music'
urlpatterns = [
    path('',HomePage.as_view(),name='home'),
    path('album',AlbumList.as_view(),name='album-list'),
    path('album/<int:pk>',SongAlbum.as_view(),name='SongAlbum'),
    path('album/<int:album_id>/vote',CreateVote.as_view(),name='CreateVote'),
    path('album/<int:album_id>/vote/<int:pk>',UpdateVote.as_view(),name='UpdateVote'),
    path('album/top',TopAlbum.as_view(),name='top_album'),
    path('album/categories/rap',Categories.as_view(),name='rap'),
    path('album/categories/rap/<int:pk>',SongAlbum.as_view(),name='RapAlbum'),
    path('album/categories/rock',Categories.as_view(),name='rock'),
    path('album/categories/rock/<int:pk>',SongAlbum.as_view(),name='RockAlbum')
]