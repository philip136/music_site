from django.urls import path
from .views import (CommentAPIView,
                    CommentCreateAPIView,
                    CommentUpdateAPIView)



urlpatterns = [
    path('', CommentAPIView.as_view(), name='albums'),
    path('create/', CommentCreateAPIView.as_view(), name='create'),
    path('<int:pk>/edit/', CommentUpdateAPIView.as_view(), name='update')
]