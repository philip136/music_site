"""music_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
import users.urls
import music.urls
import music.comments.urls
import chat_room.urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(users.urls), name='user'),
    path('', include('django.contrib.auth.urls')),
    path('', include(music.urls), name='music'),
    path('api/albums/', include(music.comments.urls), name='albums-api'),
    path('api/chat/', include(chat_room.urls), name='chat-api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_verify'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
