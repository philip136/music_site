from django.urls import path
from .views import (AlbumAPIView,
                    DetailAlbumAPIView,
                    AlbumUpdateAPIView,
                    AlbumDeleteAPIView,
                    AlbumCreateAPIView,
                    )


urlpatterns = [
    path('', AlbumAPIView.as_view(), name='albums'),
    path('<int:pk>/', DetailAlbumAPIView.as_view(), name='detail'),
    path('create/', AlbumCreateAPIView.as_view(), name='create'),
    path('<int:pk>/edit/', AlbumUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', AlbumDeleteAPIView.as_view(), name='delete'),
]