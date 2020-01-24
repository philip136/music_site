from django.conf import settings
from django.contrib.auth import (SESSION_KEY,
                                 BACKEND_SESSION_KEY,
                                 HASH_SESSION_KEY,

                                 )
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from users.models import Profile


def create_session_cookie(username, password):
    user = User.objects.create_user(username=username, password=password)
    profile = Profile.objects.get(user=user)
    session = SessionStore()
    session[SESSION_KEY] = profile.pk
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session[HASH_SESSION_KEY] = user.get_session_auth_hash()
    session.save()
    cookies = {
        "name": settings.SESSION_COOKIE_NAME,
        "value": session.session_key,
        "secure": False,
        "path": "/",
    }
    return cookies